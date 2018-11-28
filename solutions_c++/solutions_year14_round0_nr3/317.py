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

const int nmax = 55;

const int dx[] = { -1, 1, 0, 0, -1, 1, -1, 1 };
const int dy[] = { 0, 0, -1, 1, -1, -1, 1, 1 };

int used[nmax][nmax];
int a[nmax][nmax];
int n, m, k;

bool in(int x, int y)
{
	return 0 <= x && x < n && 0 <= y && y < m;
}

int getCnt(int x, int y)
{
	int ret = 0;
	for (int i = 0; i < 8; i ++)
	{
		int nx = x + dx[i], ny = y + dy[i];
		if (in(nx,ny) && a[nx][ny])
			ret++;
	}
	return ret;
}

int dfs(int x, int y)
{
	if (!in(x,y)) return 0;
	if (used[x][y]) return 0;
	if (a[x][y]) return 0;
	
	used[x][y] = true;
	int ret = 1;
	if (getCnt(x,y) > 0) return ret;

	for (int i = 0; i < 8; i ++)
		ret += dfs(x + dx[i], y + dy[i]);

	return ret;
}

bool check(int x, int y)
{
	if (a[x][y]) return false;
	_(used, 0);
	int cntFree = 0;
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			if (!a[i][j])
				cntFree++;
		}
	}
	assert(cntFree == n * m - k);
	return dfs(x, y) == cntFree;
}

void build_field(int rx, int ry, int cx, int cy)
{
	assert(rx * ry + cx + cy == n * m - k);
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j ++)
			a[i][j] = 1;
	for (int i = 0; i < rx; i ++)
	{
		for (int j = 0; j < ry; j ++)
		{
			a[i][j] = 0;
		}
	}
	for (int i = 0; i < cx; i ++)
		a[i][ry] = 0;
	for (int j = 0; j < cy; j ++)
		a[rx][j] = 0;
}

void print_field(int x, int y)
{
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			printf("%c", (i == x && j == y) ? 'c' : (a[i][j] ? '*' : '.'));
		}
		printf("\n");
	}
}

bool check_field()
{
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			if (check(i, j))
			{
				print_field(i, j);
				return true;
			}
		}
	}
	return false;
}

bool rec(int x, int y, int lft)
{
	if (lft == 0)
		return check_field();
	if (x == n) return false;
	if (y == m)
		return rec(x + 1, 0, lft);
	
	a[x][y] = 0;
	lft--;
	if (rec(x, y + 1, lft))
		return true;
	
	lft++;
	a[x][y] = 1;
	if (rec(x, y + 1, lft))
		return true;
	return false;
}

bool stupid()
{
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < m; j ++)
			a[i][j] = 1;
	int lft = n * m - k;
	return rec(0, 0, lft);
}

bool solve()
{
	_(a, 0);
	scanf("%d%d%d",&n,&m,&k);
	
	for (int rx = 1; rx <= n; rx ++)
	{
		for (int ry = 1; ry <= m; ry ++)
		{
			int cxBound = ry == m ? 0 : rx;
			int cyBound = rx == n ? 0 : ry;
			for (int cx = 0; cx <= cxBound; cx ++)
			{
				for (int cy = 0; cy <= cyBound; cy ++)
				{
					if (rx * ry + cx + cy == n * m - k)
					{
						build_field(rx, ry, cx, cy);
						if (check_field())
							return false;
					}
				}
			}
		}
	}
	printf("Impossible\n");
	//assert(!stupid());
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
		printf("Case #%d:\n", i + 1);
		solve();
	}
	return 0;
}
