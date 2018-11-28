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

const int nmax = 10005;

int n, x, s[nmax];

void read()
{
	scanf("%d%d",&n,&x);
	for (int i = 0; i < n; i ++)
		scanf("%d",&s[i]);
}

bool used[nmax];
vector < pair < short, short > > g[nmax];

bool solve()
{
	read();
	for (int i = 0; i < n; i ++)
		used[i] = 0;
	for (int i = 0; i < nmax; i ++)
		g[i].clear();

	for (int i = 0; i < n; i ++)
	{
		g[s[i]].pb(mp(i,-1));
		for (int j = i + 1; j < n; j ++)
		{
			if (s[i] + s[j] <= x)
			{
				g[s[i] + s[j]].pb(mp(i,j));
			}
		}
	}
	
	int ans = 0;
	for (int i = x; i >= 0; i --)
	{
		for (int j = 0; j < sz(g[i]); j ++)
		{
			int x = g[i][j].first, y = g[i][j].second;
			if (!used[x] && (y == -1 || !used[y]))
			{
				ans++;
				used[x] = true;
				if (y != -1)
					used[y] = true;
			}
		}
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
		solve();
	}
	return 0;
}
