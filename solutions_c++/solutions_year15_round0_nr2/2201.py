#include <stdio.h>
#include <stdlib.h>

#define MAXN 1100

int n, p[MAXN];

int max(int x, int y)
{
	return x > y ? x : y;
}

int min(int x, int y)
{
	return x < y ? x : y;
}

int main()
{
	int T, ans;
	scanf("%d", &T);

	for (int test = 1; test <= T; test++)
	{
		scanf("%d", &n);

		ans = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &p[i]);
			ans = max(ans, p[i]);
		}

		int cakes = ans;
		for (int i = 1; i < cakes; i++)
		{
			int time = i;
			for (int j = 0; j < n; j++)
				time += (p[j] - 1) / i;

			ans = min(ans, time);
		}

		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}
