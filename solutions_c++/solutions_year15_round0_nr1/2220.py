#include <stdio.h>
int s, t, i, j, now, ans;
char str[1005];


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%d%s", &s, str);
		now = ans = 0;
		for (j = 0; j <= s; j++)
		{
			if (str[j] - '0' && now < j)
			{
				ans += j - now;
				now = j + str[j] - '0';
			}
			else
			{
				now += str[j] - '0';
			}
		}
		printf("Case #%d: %d\n", i, ans);

	}
	return 0;
}