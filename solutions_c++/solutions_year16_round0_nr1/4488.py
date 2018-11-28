#include<stdio.h>

int main(void)	{
	int test, T;
	int i, k, n, t;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);

	for (test = 1; test <= T; test++)	{
		bool chk[10] = { 0 };

		scanf("%d", &n);

		k = 0;
		for (i = 1; i <= 1000; i++)	{
			t = n * i;
			while (t)	{
				if (chk[t % 10] == 0)	{
					k++;
					chk[t % 10] = 1;
				}

				t /= 10;
			}

			if (k == 10)
				break;
		}

		printf("Case #%d: ", test);
		if (k == 10)
			printf("%d\n", n * i);
		else
			printf("INSOMNIA\n");
	}

	return 0;
}