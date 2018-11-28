#include <cstdio>

char s[1001];

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		int level;
		scanf("%d %s", &level, s);

		int sum = s[0] - 48;
		int ans = 0;
		for (int i = 1; i <= level; ++i)
		{
			if (sum < i)
			{
				ans += i - sum;
				sum = i;
			}

			sum += s[i] - 48;
		}

		printf("Case #%d: %d\n", t, ans);
	}
	
	return 0;
}
