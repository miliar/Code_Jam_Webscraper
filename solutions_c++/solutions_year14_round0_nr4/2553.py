#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int test, tt, ok[1005];
int ans1, ans2, i, j, n;
double a[1005], b[1005];

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--)
	{
		scanf("%d", &n);
		for (i = 1; i <= n; i++)
			scanf("%lf", &b[i]), ok[i] = 1;
		for (i = 1; i <= n; i++)
			scanf("%lf", &a[i]);
		sort(a + 1, a + n + 1);
		sort(b + 1, b + n + 1);
		for (i = n; i >= 0; i--)
		{
			for (j = 1; j <= i; j++)
				if (a[j] > b[n - i + j])
					break;
			if (j > i)
				break;
		}
		
		ans1 = i;
		ans2 = 0;
		for (i = n; i >= 1; i--)
		{
			for (j = 1; j <= n; j++)
				if (ok[j] && a[j] > b[i])
					break;
			if (j <= n)
				ok[j] = 0;
			else
			{
				for (j = 1; j <= n; j++)
					if (ok[j])
						break;
				ok[j] = 0;
				ans2++;
			}
		}
		
		printf("Case #%d: %d %d\n", ++tt, ans1, ans2);
	}
	
	return 0;
}
