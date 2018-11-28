#include <iostream>
#include <stdio.h>
using namespace std;

const int maxn = 1010;
int a[maxn];

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	for(int iCase = 1; iCase <= T; iCase++)
	{
		int n;
		scanf("%d", &n);

		int maxm = 0;

		for(int i = 1; i <= n; i++)
		{
			scanf("%d", &a[i]);
			maxm = max(maxm, a[i]);
		}
		int ans = 1000000000;
		for(int high = 1; high <= maxm; high++)
		{
			int sum = high;
			for(int i = 1; i <= n; i++)
			{
				if(a[i] > high)
				{
					sum += a[i] / high - (a[i] % high == 0);
				}
			}
			ans  = min(ans, sum);
		}

		printf("Case #%d: %d\n", iCase, ans);

	}

	return 0;
}
