#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
	int t, n;
	double a[1111];
	double b[1111];
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
			scanf("%lf", &a[j]);
		for (int j = 0; j < n; j++)
			scanf("%lf", &b[j]);

		sort(a, a + n);
		sort(b, b + n);

		int k = n - 1;
		int ansA = n, ansB = 0;
		for (int j = n - 1; j >= 0; j--)
		{
			while (k >= 0 && b[k] > a[j])
				k--;
			if (k < 0)
			{
				ansA = n - j - 1;
				break;
			}
			k--;
		}

		
		k = 0;
		for (int j = 0; j < n; j++)
		{
			while (k < n && b[k] < a[j])
				k++;
			if (k >= n)
			{
				ansB = n - j;
				break;
			}
			k++;
		}
		printf("Case #%d: %d %d\n", i, ansA, ansB);
	}
	return 0;
}