#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <algorithm>

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		int n;
		scanf("%d", &n);
		double a[1010], b[1010];
		for (int i = 0; i < n; i++)
			scanf("%lf", &a[i]);
		for (int i = 0; i < n; i++)
			scanf("%lf", &b[i]);
		std::sort(a, a + n);
		std::sort(b, b + n);
		int decWarRes = 0, warRes = n;
		int j = n - 1;
		for (int i = n - 1; i >= 0 && j >= 0; i--)
		{
			if (j >= 0 && a[j] > b[i])
			{
				decWarRes++;
				j--;
			}
		}
		j = n - 1;
		for (int i = n - 1; i >= 0 && j >= 0; i--)
		{
			if (j >= 0 && b[j] > a[i])
			{
				warRes--;
				j--;
			}
		}
		printf("Case #%d: %d %d\n", k, decWarRes, warRes);
	}
	return 0;
}