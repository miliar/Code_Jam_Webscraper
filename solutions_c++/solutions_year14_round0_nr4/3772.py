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
#define MAXN 1001

int n;
double a[MAXN];
double b[MAXN];
int p[MAXN];
int ok[MAXN];
int d[MAXN][MAXN];

inline void solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%lf", &a[i]);
	for (int i = 0; i < n; ++i)
		scanf("%lf", &b[i]);

	sort(a, a + n);
	sort(b, b + n);

	for (int i = 0; i < n; ++i)
		ok[i] = 0;

	int s = 0;
	for (int i = 0; i < n; ++i)
	{
		double t = a[i];
		int ind = -1;
		for (int j = 0; j < n; ++j)
			if (!ok[j] && t < b[j])
			{
				ind = j;
				break;
			}
		if (ind == -1)
		{
			for (int j = 0; j < n; ++j)
				if (!ok[j])
				{
					ind = j;
					break;
				}
			s++;
		}

		ok[ind] = 1;
	}

	d[0][0] = a[0] > b[0];
   for (int i = 0; i < n; ++i)
   	for (int j = 0; j < n; ++j)
   	{
   		if (i + j == 0) continue;

   		d[i][j] = 0;
   		if (i)
   			d[i][j] = max(d[i][j], d[i - 1][j]);
   		if (j)
   			d[i][j] = max(d[i][j], d[i][j - 1]);

   		if (a[i] > b[j])
   			d[i][j] = max(d[i][j], 1 + (i && j ? d[i - 1][j - 1] : 0));
   	}
	printf("%d %d\n", d[n - 1][n - 1], s);
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
