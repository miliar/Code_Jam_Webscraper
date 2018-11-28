#include <stdio.h>

#define MAXS 1100

int main()
{
	int T;
	scanf("%d", &T);

	int n;
	char s[MAXS];

	for (int testcase = 1; testcase <= T; testcase++)
	{
		scanf("%d%s", &n, s);

		int ans = 0, standing = 0;
		for (int i = 0; i <= n; i++)
		{
			if (standing < i)
			{
				ans += i - standing;
				standing += i - standing;
			}

			standing += s[i] - '0';
		}

		printf("Case #%d: %d\n", testcase, ans);
	}

	return 0;
}
