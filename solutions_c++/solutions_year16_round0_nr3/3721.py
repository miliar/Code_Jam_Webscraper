#include <stdio.h>
#include <memory.h>
#include <iostream>

#define N 32
#define M 500

int jamcoin[N + 10];
int n, m;

void addone()
{
	int i = n - 2;
	jamcoin[i] ++;
	while (jamcoin[i] > 1 && i >= 0)
	{
		jamcoin[i] = 0;
		jamcoin[i - 1] ++;
		i--;
	};
}

int main()
{
	int c, cnt = 0;
	__int64  divider[11];
	scanf("%d%d%d", &c, &n, &m);
	printf("Case #1:\n");
	
	memset(jamcoin, 0, sizeof(jamcoin));
	jamcoin[0] = jamcoin[n-1] = 1;

	for (;;)
	{
		bool flag = true;

		for (int i = 2; i <= 10; i++)
		{
			__int64 a = 0;
			for (int j = 0; j < n; j++)
			{
				a *= i;
				a += jamcoin[j];
			}

			bool isPrime = true;
			for (__int64 k = 2; k*k < a; k++)
			{
				__int64 temp = a % k;
				if (temp == 0)
				{
					divider[i] = k;
					isPrime = false;
					break;
				}
			}

			if (isPrime) 
			{
				flag = false;
				break;
			}
		}

		if (flag)
		{
			cnt++;
			if (cnt % 10 == 0)
			{
				FILE *out = fopen("count.txt", "wt");
				fprintf(out, "%d\n", cnt);
				fclose(out);
			}
			for (int j = 0; j < n; j++)
				printf("%d", jamcoin[j]);
			for (int j = 2; j <= 10; j++)
				std::cout << " " << divider[j];
			printf("\n");
			if (cnt == m)
				return 0;
		}

		addone();
	}
}