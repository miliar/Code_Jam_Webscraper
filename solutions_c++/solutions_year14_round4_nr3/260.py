#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <deque>
#include <cassert>

using namespace std;

#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

typedef long long ll;

#define F first
#define S second
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define sz(s) (int(s.size()))
#define fname "a"
#define ms(a,x) memset(a, x, sizeof(a))
#define forit(it,s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define MAXN 505
#define MAXE 500000

int n, m, w;
int S, T;
int a[MAXN][MAXN];
int e;
int to[MAXE];
int f[MAXE];
int c[MAXE];
vector <int> g[MAXN * MAXN * 2];
int mark[MAXN * MAXN * 2];
int cc;

inline void addEdge(int v1, int v2)
{
	f[e] = 0;
	c[e] = 1;
	to[e] = v2;
	g[v1].pb(e);
	++e;
	f[e] = 0;
	c[e] = 0;
	to[e] = v1;
	g[v2].pb(e);
	++e;
}

inline bool dfs(int v)
{
	if (v == T) return 1;
	mark[v] = cc;
	for (int i = 0; i < sz(g[v]); ++i)
	{
		int ind = g[v][i];
		int v2 = to[ind];
		if (mark[v2] != cc && f[ind] + 1 <= c[ind] && dfs(v2))
		{
			++f[ind];
			--f[ind ^ 1];
			return 1;
		}
	}
	return 0;
}

inline void solve()
{
	e = 0;
	memset(a, 0, sizeof(a));

	scanf("%d%d%d", &m, &n, &w);
	for (int z = 0; z < w; ++z)
	{
		int x1, x2, y1, y2;
		scanf("%d%d%d%d", &y1, &x1, &y2, &x2);
		for (int i = x1; i <= x2; ++i)
			for (int j = y1; j <= y2; ++j)
				a[i][j] = 1;
	}
	S = n * m * 2, T = S + 1;

	for (int i = 0; i <= T; ++i)
		g[i].clear();

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			if (a[i][j]) continue;
			int ind = i * m + j;
			addEdge(ind, ind + n * m);
			for (int dx = -1; dx <= 1; ++dx)
				for (int dy = -1; dy <= 1; ++dy)
					if (abs(dx) + abs(dy) == 1)
					{
						int sx = i + dx;
						int sy = j + dy;
						if (0 <= sx && sx < n && 0 <= sy && sy < m && !a[sx][sy])
						{
							int ind2 = sx * m + sy;
							addEdge(ind + n * m, ind2);
						}
					}
		}

	for (int i = 0; i < m; ++i)
	{
		int ind = i;
		addEdge(S, ind);
	}

	for (int i = 0; i < m; ++i)
	{
		int ind = (n - 1) * m + i;
		addEdge(ind + n * m, T);
	}

	++cc;
	int ans = 0;
	while(dfs(S))
	{
		++cc;
		++ans;
	}
	printf("%d\n", ans);
}

int main()
{
	#ifdef LOCAL
	freopen(fname".in", "r", stdin);
	freopen(fname".out", "w", stdout);
	#endif

	int tt;
	scanf("%d", &tt);
	for (int t = 0; t < tt; ++t)
	{
		printf("Case #%d: ", t + 1);
		solve();
	}
	return 0;
}
