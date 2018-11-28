#ifdef WIN32
#pragma warning(disable:4996)
#endif

#include <stdio.h>
#include <math.h>

unsigned long long int get_base_value(unsigned long long int n, int base, int binary_digits_count)
{
	unsigned long long int mask = 1;
	unsigned long long int value = 0;
	unsigned long long int power = 1;

	for (int i = 0; i < binary_digits_count; i++)
	{
		value += (((n & mask) >> i) * power);
		mask <<= 1;
		power *= base;
	}

	return value;
}

unsigned long long int get_non_trivial_divisor(unsigned long long int n)
{
	unsigned long long int square_root = (unsigned long long int) sqrt((double) n);
	unsigned long long int divisor = 0;

	for (unsigned long long int i = 2; i < square_root; i++)
	{
		if (n % i == 0)
		{
			divisor = i;
			break;
		}
	}

	return divisor;
}

void print_binary(unsigned long long int value, int n)
{
	char s[33];
	int i = n - 1;

	s[n] = '\0';
	while (value != 0)
	{
		s[i] = '0' + value % 2;
		value /= 2;
		i--;
	}

	fprintf(stdout, s);
}

int main(int argc, char *argv[])
{
	FILE *fp;
	int t = 0;
	int n = 0, j = 0;
	unsigned long long int start_base_10 = 0;
	unsigned long long int end_base_10 = 0;
	int jam_coins;
	unsigned long long int base3, base4, base5, base6, base7, base8, base9, base10;
	unsigned long long int ntd_base2, ntd_base3, ntd_base4, ntd_base5, ntd_base6, ntd_base7, ntd_base8, ntd_base9, ntd_base10;

#ifdef TESTING
	fp = fopen(argv[1], "r");
#else
	fp = stdin;
#endif

	fscanf(fp, "%d", &t);
	fscanf(fp, "%d %d", &n, &j);

	fprintf(stdout, "Case #1:\n");

	if (n == 6)
	{
		start_base_10 = 33; //100001
		end_base_10 = 77; //111111
	}
	else if (n == 16)
	{
		start_base_10 = 32769; //1000000000000001
		end_base_10 = 65536; //1111111111111111
	}
	else if (n == 32)
	{
		start_base_10 = 2147483649; //10000000000000000000000000000001
		end_base_10 = 4294967295; //11111111111111111111111111111111
	}

	if (start_base_10 > 0)
	{
		jam_coins = 0;
		for (unsigned long long int i = start_base_10; i <= end_base_10; i += 2)
		{
			ntd_base2 = get_non_trivial_divisor(i);
			if (ntd_base2 == 0)
			{
				continue;
			}

			base3 = get_base_value(i, 3, n);
			ntd_base3 = get_non_trivial_divisor(base3);
			if (ntd_base3 == 0)
			{
				continue;
			}

			base4 = get_base_value(i, 4, n);
			ntd_base4 = get_non_trivial_divisor(base4);
			if (ntd_base4 == 0)
			{
				continue;
			}

			base5 = get_base_value(i, 5, n);
			ntd_base5 = get_non_trivial_divisor(base5);
			if (ntd_base5 == 0)
			{
				continue;
			}

			base6 = get_base_value(i, 6, n);
			ntd_base6 = get_non_trivial_divisor(base6);
			if (ntd_base6 == 0)
			{
				continue;
			}

			base7 = get_base_value(i, 7, n);
			ntd_base7 = get_non_trivial_divisor(base7);
			if (ntd_base7 == 0)
			{
				continue;
			}

			base8 = get_base_value(i, 8, n);
			ntd_base8 = get_non_trivial_divisor(base8);
			if (ntd_base8 == 0)
			{
				continue;
			}

			base9 = get_base_value(i, 9, n);
			ntd_base9 = get_non_trivial_divisor(base9);
			if (ntd_base9 == 0)
			{
				continue;
			}

			base10 = get_base_value(i, 10, n);
			ntd_base10 = get_non_trivial_divisor(base10);
			if (ntd_base10 == 0)
			{
				continue;
			}

			print_binary(i, n);
			fprintf(stdout, " %llu %llu %llu %llu %llu %llu %llu %llu %llu\n", ntd_base2, ntd_base3, ntd_base4, ntd_base5, ntd_base6, ntd_base7, ntd_base8, ntd_base9, ntd_base10);
			jam_coins++;
			if (jam_coins == j)
			{
				break;
			}
		}
	}

#ifdef TESTING
	fclose(fp);
#endif
}
