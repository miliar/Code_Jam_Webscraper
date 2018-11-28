#include <cstdio>
int a[2001] = {0};
int main()
{
	int T, tt;
	freopen("Al.in", "r", stdin);
	freopen("Al.out", "w", stdout);
	scanf("%d", &T);
	for (tt = 0; tt < T; tt++)
	{
		int n;
		scanf("%d", &n);
		int ans = 0, now = 0;
		for (int i = 0; i <= n; i++)
		{
			scanf("%1d", &a[i]);
			if (now >= i)
				now += a[i];
			else
			{
				ans += (i-now);
				now += (i-now);
				now += a[i];
			}
		}
		printf("Case #%d: %d\n", tt+1, ans);
	}
	return 0;
}
