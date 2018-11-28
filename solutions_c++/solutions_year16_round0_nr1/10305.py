#include <cstdio>

int main()
{
	int n, i, j, N, m, cnt;
	bool digits[10];

	freopen("input.txt", "r", stdin);
	freopen("output.out", "w", stdout);

	for (scanf("%d", &n), i = 1; i <= n; i++)
	{
		cnt = 1;
		for (j = 0; j < 10; j++)
		{
			digits[j] = false;
		}
		scanf("%d", &N);

		while (N!=0)
		{
			m = N*cnt;

			while (m != 0)
			{
				digits[m % 10] = true;
				m /= 10;
			}

			for (j = 0; j < 10; j++)
				if (digits[j] == false)
					break;

			if (j == 10)
				break;

			cnt++;
		}
		
		if (N == 0)
			printf("Case #%d: INSOMNIA\n", i);
		else
			printf("Case #%d: %d\n", i, N*cnt);

	}
}