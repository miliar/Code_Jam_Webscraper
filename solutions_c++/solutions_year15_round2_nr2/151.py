#define _CRT_SECURE_NO_DEPRECATE
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

bool bit(int msk, int i)
{
	return msk & (1 << i);
}

int cntbit(int msk, int n)
{
	int ret = 0;
	for (int i = 0; i < n; i ++)
		ret += bit(msk, i);
	return ret;
}

const int nmax = 10005;

vector < int > cands;
int lft, n, m, need;
bool busy[nmax][nmax];

void read()
{
	scanf("%d%d%d", &n, &m, &need);
}

void init()
{
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			busy[i][j] = 0;
		}
	}
	lft = need;
	cands.clear();
}

bool in(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, -1, 0, 1 };

bool canPlace(int x, int y)
{
	if (busy[x][y]) 
		return false;
	for (int i = 0; i < 4; i ++)
	{
		int nx = x + dx[i], ny = y + dy[i];
		if (in(nx, ny) && busy[nx][ny])
			return false;
	}
	return true;
}

int calcBusyNeighbors(int x, int y)
{
	int ret = 0;
	for (int i = 0; i < 4; i ++)
	{
		int nx = x + dx[i], ny = y + dy[i];
		if (in(nx, ny) && busy[nx][ny])
			ret++;
	}
	return ret;
}

int calcCost(int msk)
{
	init();
	int ret = 0;
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			int id = i * m + j;
			if (bit(msk, id))
				busy[i][j] = 1;
		}
	}
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			int id = i * m + j;
			if (bit(msk, id))
				ret += calcBusyNeighbors(i, j);
		}
	}
	return ret / 2;
}

bool solve()
{
	int ans = INF;
	for (int msk = 0; msk < (1 << (n * m)); msk ++)
	{
		if (cntbit(msk, n * m) != need)
			continue;
		ans = min(ans, calcCost(msk));
	}
	printf("%d\n", ans);
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
