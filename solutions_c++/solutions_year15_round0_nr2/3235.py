#include <cstdio>
int T, n, a[1111];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		int ans = 1000;
		for (int i = 1; i <= 1000; i++)
		{
			int sum = 0;
			for (int j = 0; j < n; j++)
				sum += (a[j] - 1) / i;
			if (sum + i < ans)
				ans = sum + i;
		}
		printf("Case #%d: %d\n", tt, ans);
	}
}