#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;
main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int nc;
	int t = 0;
	scanf("%d", &nc);
	while (t++ < nc)
	{
		int n;
		int i, j;
		double a[1001], b[1001];
		int c[1001];
		scanf("%d", &n);
		for (i = 0; i < n; i++)
		{
			scanf("%lf", &a[i]);
		}
		for (i = 0; i < n; i++)
		{
			scanf("%lf", &b[i]);
			c[i] = 0;
		}
		sort(a, a+n);
		sort(b, b+n);
		int v1=0, v2=0;
		j = 0;
		for (i = 0; i < n; i++)
		{
			if (a[i] < b[j]) {
				v1 ++;
			}
			else j++;
		}
		for (i = 0; i < n; i++)
		{
			int l = 0;
			if (l >= n)
			{
				break;
			}
			for (j = l; j < n; j++)
			{
				if (b[j] > a[i] && c[j] == 0)
				{
					c[j] = 1;
					v2++;
					l = j+1;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n", t, n-v1, n-v2);
	}
	return 0;
}