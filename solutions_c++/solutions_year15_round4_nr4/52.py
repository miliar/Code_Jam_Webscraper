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

const int nmax = 6;

int dx[] = { -1, 0, 1, 0 };
int dy[] = { 0, -1, 0, 1 };

int n, m;
set < vector < int > > q;
int a[nmax][nmax];
vector < vector < int > > cands;
vector < int > buf;

vector < int > getAns()
{
	buf.clear();
	cands.clear();
	for (int startCol = 0; startCol < m; startCol ++)
	{
		buf.clear();
		for (int col = startCol, cntCol = 0; cntCol < m; cntCol ++, col = (col + 1) % m)
		{
			for (int row = 0; row < n; row ++)
			{
				buf.pb(a[row][col]);
			}
		}
		cands.pb(buf);
	}
	sort(all(cands));
	return cands[0];
}

void read()
{
	scanf("%d%d",&n,&m);
}

bool isIn(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

bool isOk(int x, int y)
{
	int cntSame = 0;
	for (int i = 0; i < 4; i ++)
	{
		int nx = x + dx[i], ny = (y + dy[i] + m) % m;
		if (isIn(nx,ny) && a[x][y] == a[nx][ny])
		{
			cntSame++;
		}
	}
	return cntSame == a[x][y];
}

void rec(int x, int y)
{
	if (y == m)
	{
		rec(x + 1, 0);
		return;
	}
	if (x == n)
	{
		for (int col = 0; col < m; col ++)
		{
			if (!isOk(n - 1, col))
			{
				return;
			}
		}
		q.insert(getAns());
		return;
	}

	for (int val = 1; val <= 3; val ++)
	{
		a[x][y] = val;
		if (!isIn(x - 1, y) || isOk(x - 1, y))
		{
			rec(x, y + 1);
		}
		a[x][y] = -1;
	}
}

bool solve()
{
	_(a, -1);
	q.clear();
	rec(0, 0);
	printf("%d\n", sz(q));
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
