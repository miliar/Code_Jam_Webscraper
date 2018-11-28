#include <cstdio>
const int maxn = 1005;
int n, a[maxn], ans;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		ans = 1000;
		for (int i = 1; i <= 1000; i++)
		{
			int sum = 0;
			for (int j = 1; j <= n; j++)
				sum += (a[j] - 1) / i;
			if (sum + i < ans)
				ans = sum + i;
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}
