#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int XMAX = 10000;
const int nmax = 10005;
const int MAGIC = 10000000;

bool in(int x, int y)
{
	return -XMAX <= x && x <= +XMAX && 0 <= y && y <= XMAX;
}

int dx[] = { -2, -1, 0, +1, +2 };
int dy[] = { 0, +1, +2, +1, 0 };

vector < pii > ord[nmax];
map < pii , int > mem;
queue < pii > q;

void upd(int x, int y, int cost)
{
	if (mem.find(mp(x,y)) == mem.end())
	{
		q.push(mp(x,y));
		mem[mp(x,y)] = cost;
	}
}

void precalc()
{
	upd(0, 0, 0);
	while (!q.empty())
	{
		if (sz(mem) > MAGIC) break;
		int x = q.front().first, y = q.front().second;
		q.pop();
		int cost = mem[mp(x,y)];
		ord[cost].pb(mp(x,y));
		for (int i = 0; i < 5; i ++)
		{
			int nx = x + dx[i], ny = y + dy[i];
			if (in(nx,ny))
				upd(nx, ny, cost + 1);
		}
	}
	for (int i = 0; i < nmax; i ++)
		sort(all(ord[i]));
}

double dp[nmax][nmax];

bool solve()
{
	lint n, x, y, k;
	int m;
	scanf("%lld%lld%lld",&n,&x,&y);
	for (k = 0; ; k ++)
	{
		lint total = k * 4 + 1;
		if (n > total)
			n -= total;
		else
			break;
	}
	if (mem.find(mp(x,y)) == mem.end() || mem[mp(x,y)] > k)
	{
		printf("0.0\n");
		return false;
	}
	if (mem[mp(x,y)] < k || n == k * 4 + 1)
	{
		printf("1.0\n");
		return false;
	}
	_(dp, 0);
	m = k * 2;

	pii key = mp(x,y);
	int id = lower_bound(all(ord[k]), key) - ord[k].begin();
	if (n < k * 4 + 1 && id == m)
	{
		printf("0.0\n");
		return false;
	}

	dp[0][0] = 1;
	for (int i = 0; i < n; i ++)
	{
		for (int a = 0; a <= m; a ++)
		{
			int b = i - a;
			if (a == m)
			{
				dp[i + 1][a] += dp[i][a];
			}
			else
			if (b == m)
			{
				dp[i + 1][a + 1] += dp[i][a];
			}
			else
			{
				dp[i + 1][a] += dp[i][a] * 0.5;
				dp[i + 1][a + 1] += dp[i][a] * 0.5;
			}
		}
	}

	if (id > m) id = m - 1 - (id - m - 1);
	id++;
	double ans = 0.0;
	for (int i = id; i <= m; i ++)
		ans += dp[n][i];
	printf("%.12lf\n", ans);
	return false;
}

int main()
{
	precalc();
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
