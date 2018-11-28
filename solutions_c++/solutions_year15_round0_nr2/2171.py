#include <stdio.h>
#include <algorithm>
using namespace std;
int d, t, i, j, ans, p[1005], now, k;



int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%d", &d);
		for (j = 0; j < d; j++)
			scanf("%d", p + j);
		sort(p, p + d);
		ans = p[d-1];

		for (j = 1; j < p[d - 1]; j++)
		{
			now = 0;
			for (k = 0; k < d; k++)
			{
				if (p[k]>j)
				{
					now += (p[k] - 1) / j;
				}
			}
			if (now + j < ans)
				ans = now + j;
		}

		printf("Case #%d: %d\n", i, ans);

	}
	return 0;
}