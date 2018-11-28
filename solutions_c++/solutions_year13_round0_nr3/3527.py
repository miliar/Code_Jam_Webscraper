#include <iostream>
#include <math.h>

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");


int T;
long long A, B;

bool isPalindrom(long long x)
{
	int a[100];
	int n = 0;
	while (x > 0)
	{
		a[n++] = x % 10;
		x = x / 10;
	}
	for (int j = 0; j < n / 2; ++j)
	{
		if (a[j] != a[n - j - 1])
		{
			return false;
		}
	}
	return true;
}

int main()
{
	fscanf(f, "%d", &T);
	for (int t = 0; t < T; ++t)
	{
		fscanf(f, "%lld %lld", &A, &B);
		int rez = 0;
		for (long long i = A; i <= B; ++i)
		{
			if (isPalindrom(i))
			{
				long long x = sqrtl(i);
				if (x * x  == i && isPalindrom(x))
				{
					rez++;
				}
			}
		}

		fprintf(g, "Case #%d: %d\n", t + 1, rez);
	}

	return 0;
}