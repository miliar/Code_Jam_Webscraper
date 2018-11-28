#include <cstdio>

int ten[10];

int main() {
	int T, N;

	//freopen("input1.txt", "r", stdin);
	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &N);

		for (int i = 0; i < 10; i++)
			ten[i] = 0;
		
		int i;
		for (i = 1; i < 2000; i++)
		{
			long long n = N * i;

			while (n != 0)
			{
				int a = n % 10;
				n /= 10;
				ten[a] = 1;
			}

			bool flag = true;
			for (int j = 0; j < 10; j++)
			{
				if (ten[j] == 0)
				{
					flag = false;
					break;
				}
			}

			if (flag)
			{
				printf("Case #%d: %lld\n", t, (long long)(i * N));
				break;
			}
		}

		if (i == 2000)
			printf("Case #%d: INSOMNIA\n", t);
	}

	return 0;
}
