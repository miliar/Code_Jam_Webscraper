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
#ifdef _DEBUG
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

const int nmax = 105;

int a[nmax][nmax];
bool can[nmax][nmax];
bool used[nmax][nmax];
int n, m, total;

bool goodCol(int j)
{
	for (int i = 0; i < n; i ++)
	{
		if (!can[i][j]) return false;
	}
	return true;
}

void paintCol(int j)
{
	for (int i = 0; i < n; i ++)
		used[i][j] = true;
}

bool goodRow(int i)
{
	for (int j = 0; j < m; j ++)
	{
		if (!can[i][j]) return false;
	}
	return true;
}

void paintRow(int i)
{
	for (int j = 0; j < m; j ++)
		used[i][j] = true;
}

int covered(int lvl)
{
	_(used, 0);
	for (int i = 0; i < n; i ++)
	{
		if (goodRow(i))
			paintRow(i);
	}
	for (int j = 0; j < m; j ++)
	{
		if (goodCol(j))
			paintCol(j);
	}
	int ret = 0;
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			ret += used[i][j] && can[i][j];
		}
	}
	return ret;
}

bool solve()
{
	scanf("%d%d",&n,&m);
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	_(can, 0);
	total = 0;
	for (int lvl = 1; lvl <= 100; lvl ++)
	{
		for (int i = 0; i < n; i ++)
		{
			for (int j = 0; j < m; j ++)
			{
				if (a[i][j] == lvl)
				{
					total ++;
					can[i][j] = true;
				}
			}
		}
		if (covered(lvl) != total)
		{
			printf("NO\n");
			return false;
		}
	}
	printf("YES\n");
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbgx(i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
