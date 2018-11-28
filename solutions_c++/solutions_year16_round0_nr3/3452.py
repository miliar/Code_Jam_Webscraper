#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int check_prime_number(unsigned long long n)
{
	if (n <= 1) return 1;
	if (n == 2) return 0;
	if (n % 2 == 0) return 2;

	int m = sqrt(n);

	for (int i = 3; i <= m; i += 2)
	{
		if (n % i == 0)
			return i;
	}

	return 0;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N, J;
		cin >> N >> J;

		printf("Case #%d:\n", t);
		int j = 0;

		for (unsigned int i = 0; i < (1 << (N - 2)); i++)
		{
			unsigned int jam = (i << 1) | (1 << (N - 1)) | 1;
			bool found = true;
			int numbers[9];

			for (int k = 2; k <= 10; k++)
			{
				long long K = 1;
				unsigned long long number = 0;
				for (int n = 0; n < N; n++)
				{
					number += ((jam >> n) & 0x1) * K;
					K *= k;
				}

				int divisor = check_prime_number(number);
				if (divisor == 0)
				{
					found = false;
					break;
				}

				numbers[k - 2] = divisor;
			}

			if (found)
			{
				char bin[32 + 1] = {};
				for (int n = 0; n < N; n++)
				{
					bin[N - 1 - n] = ((jam >> n) & 1) ? '1' : '0';
				}
				printf("%s ", bin);
				for (int k = 0; k < 9; k++)
				{
					printf("%u ", numbers[k]);
				}
				printf("\n");
				j++;

				if (j == J)
				{
					break;
				}
			}
		}


	}

	return 0;
}
