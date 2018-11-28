#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <queue>
#include <deque>
#include <cassert>
#include <string.h>
#include <iomanip>
using namespace std;

#define INF 1000000000
#define lint long long
#define mp make_pair
#define pb push_back

double d[205][205];
double p[205];
double a[205];
int n, k;

double check()
{
	for (int i = 1; i <= k; ++i)
	{
		for (int j = 0; j <= k; ++j)
		{
			d[i][j] = 0;
		}
	}

	d[0][0] = 1;

	for (int i = 1; i <= k; ++i)
	{
		d[i][0] = d[i - 1][0] * (1 - a[i]);
		for (int j = 1; j <= i && j * 2 <= k; ++j)
		{
			d[i][j] = d[i - 1][j] * (1 - a[i]) + d[i - 1][j - 1] * a[i];
		}
	}

	return d[k][k / 2];
}

int main()
{
	freopen("B-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc, T = 1;
	scanf("%d", &tc);

	while (tc--)
	{
		printf("Case #%d: ", T++);

		scanf("%d %d", &n, &k);

		for (int i = 1; i <= n; ++i)
		{
			scanf("%lf", &p[i]);
		}

		sort(p + 1, p + 1 + n);

		double ans = 0;
		for (int i = 0; i <= k; ++i)
		{
			int j = n - (k - i);
			for (int f = 1; f <= i; ++f)
			{
				a[f] = p[f];
			}

			for (int f = j + 1; f <= n; ++f)
			{
				a[i + (f - j)] = p[f];
			}

			double cur = check();
			ans = max(ans, cur);
		}

		printf("%.9f\n", ans);
	}
	return 0;
}