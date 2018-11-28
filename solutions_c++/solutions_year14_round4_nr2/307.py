#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <string>
#define lld long long
#define INF 2100000000
#define eps 1e-8
#define mem(a,b) memset(a,b,sizeof(a))

using namespace std;
int a[200000];
int main()
{
	int T;
	int n, m, i, j, cas = 0;

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> T;

	while (T--)
	{
		scanf("%d", &n);
		int maxa = 0;

		for (i = 1; i <= n; i++)
		{
			scanf("%d", &a[i]);
			maxa = max(maxa, a[i]);
		}

		int ans = 0;
		int l = 1, r = n;

		for (i = 1; i <= n; i++)
		{
			int ma, mm = INF;

			for (j = l; j <= r; j++)
				if (mm > a[j])
				{
					mm = a[j];
					ma = j;
				}

			if (abs(ma - l) <= abs(ma - r))
			{
				ans += abs(ma - l);

				for (j = ma; j > l; j--)
				{
					a[j] = a[j - 1];
				}

				l++;
			}
			else
			{
				ans += abs(ma - r);

				for (j = ma; j < r; j ++)
				{
					a[j] = a[j + 1];
				}

				r--;
			}
		}

		printf("Case #%d: %d\n", ++cas, ans);
	}

	return 0;
}
