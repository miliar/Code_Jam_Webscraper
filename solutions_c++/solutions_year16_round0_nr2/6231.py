#include <stdio.h>

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	setbuf(stdout, NULL);


	int T;
	scanf("%d", &T);


	for (int i = 1; i <= T; i++)
	{
		int ans = 0;

		char p[101] = { 0 };
		scanf("%s", p);

		char last = p[0];
		char *cur = p;

		while (*cur)
		{
			if (last != *cur)
			{
				last = *cur;
				ans++;
			}

			cur++;
		}

		if (last == '-')
			ans++;

			printf("Case #%d: %d\n", i, ans);

	}

	return 0;
}