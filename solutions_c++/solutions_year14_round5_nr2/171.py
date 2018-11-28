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
#define MAXD 1011
#define MAXN 102

int n, p, q;
int h[MAXN], g[MAXN];
int d[MAXN][MAXD][2];

inline void go(int i, int j, int t)
{
	if (!t)
	{
		for (int z = 0; z <= j; ++z)
		{
			int hrem = h[i] - z * p;
			if (hrem <= 0)
			{
				d[i + 1][j - z][!t] = max(d[i + 1][j - z][!t], d[i][j][t] + g[i]);
				break;
			}
			for (int i1 = 0; i1 <= 10; ++i1)
			{
				int i2 = i1 + 1;
				if (hrem - i1 * q <= 0)
				{
					d[i + 1][j - z + i2 - 1][t] = max(d[i + 1][j - z + i2 - 1][t], d[i][j][t]);
					break;
				}
				for (int ii = 1; ii <= i2; ++ii)
					if (hrem - i1 * q - (ii - 1) * p > 0 && hrem - i1 * q - ii * p <= 0)
						d[i + 1][j - z + i2 - ii][!t] = max(d[i + 1][j - z + i2 - ii][!t], d[i][j][t] + g[i]);
			}
		}
	}
	else
	{
		for (int z = 0; z <= j; ++z)
		{
			int hrem = h[i] - z * p;
			if (hrem <= 0)
			{
				d[i + 1][j - z][t] = max(d[i + 1][j - z][t], d[i][j][t] + g[i]);
				break;
			}
			for (int i1 = 1; i1 <= 10; ++i1)
			{
				int i2 = i1;
				if (hrem - i1 * q <= 0)
				{
					d[i + 1][j - z + i2 - 1][!t] = max(d[i + 1][j - z + i2 - 1][!t], d[i][j][t]);
					break;
				}
				for (int ii = 1; ii <= i2; ++ii)
					if (hrem - i1 * q - (ii - 1) * p > 0 && hrem - i1 * q - ii * p <= 0)
						d[i + 1][j - z + i2 - ii][t] = max(d[i + 1][j - z + i2 - ii][t], d[i][j][t] + g[i]);
			}
		}
	}
}

inline void solve()
{
	scanf("%d%d%d", &p, &q, &n);
	for (int i = 0; i < n; ++i)
		scanf("%d%d", &h[i], &g[i]);

	memset(d, 0, sizeof(d));
	d[0][0][0] = 1;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < MAXD; ++j)
			for (int t = 0; t < 2; ++t)
			{
				if (!d[i][j][t]) continue;
				go(i, j, t);
			}

	int ans = 0;
	for (int j = 0; j < MAXD; ++j)
		for (int t = 0; t < 2; ++t)
			ans = max(ans, d[n][j][t]);
	printf("%d\n", ans - 1);
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
