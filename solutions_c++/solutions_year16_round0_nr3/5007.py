#include <iostream>
#include <cstdio>

using namespace std;

void print_bit(int number, int bit_size)
{
	for (int i = 0; i < bit_size; i++)
		printf("%d", ((number >> (bit_size - 1 - i)) & 1));
}

int change_base(int number, int base_new, int bit_size)
{
	int res = 0, x = 1;
	for (int i = 0; i < bit_size; i++)
	{
		if (((number >> i) & 1) > 0)
			res += x;
		x = x * base_new;
	}
	return res;
}

int divisor(int number)
{
	for (int i = 2; i * i <= number; i++)
		if (number % i == 0)
			return i;
	return -1;
}

int div_base[11];

int main()
{
	int test_case;
	scanf("%d", &test_case);
	for (int case_cnt = 1; case_cnt <= test_case; case_cnt++)
	{
		int n, j, find = 0;
		scanf("%d%d", &n, &j);
		printf("Case #1:\n");
		for (int i = 0; find < j && i < (1 << (n - 2)); i++)
		{
			int number = 1 + (i << 1) + (1 << (n - 1));
			bool ok = true;
			for (int k = 2; ok && k <= 10; k++)
			{
				div_base[k] = divisor(change_base(number, k, n));
				if (div_base[k] < 2)
					ok = false;
			}
			if (ok)
			{
				find++;
				print_bit(number, n);
				for (int k = 2; k <= 10; k++)
					printf(" %d", div_base[k]);
				printf("\n");
			}
		}
	}
	return 0;
}














