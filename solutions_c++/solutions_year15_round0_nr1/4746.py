#include <cstdio>

int main()
{
	int t, n;
	char s[10101];
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc)
	{
		scanf("%d %s", &n, s);
		int ans = 0, cnt = s[0] - '0';
		for (int i = 1; i <= n; ++i)
		{
			if (s[i] != '0' && cnt < i)
			{
				ans += i - cnt;
				cnt = i;
			}
			cnt += s[i] - '0';
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}