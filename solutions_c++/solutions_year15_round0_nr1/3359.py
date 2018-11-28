#include <cstdio>

int n, T;
char s[11111];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++)
	{
		scanf("%d%s", &n, s);
		int cur = 0, ans = 0;
		for (int i = 0; i < n + 1; i++)
		{
			if (s[i] > '0' && cur < i)
			{
				ans += i - cur;
				cur = i;
			}
			cur += s[i] - '0';
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}