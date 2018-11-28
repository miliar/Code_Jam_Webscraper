#include<stdio.h>

int n, j;
long long A[15];
char str[20];

bool isPrime(long long a)	{
	long long i;

	if (a % 2 == 0)
		return false;

	for (i = 3; i * i <= a; i += 2)	{
		if (a % i == 0)
			return false;
	}

	return true;
}

void rec(int a)	{
	long long i, k, t1, t2;

	if (j == 0)
		return;

	if (a == n - 1)	{
		for (k = 2; k <= 10; k++)	{
			t1 = 0;
			t2 = 1;
			for (i = n - 1; i >= 0; i--)	{
				t1 += t2 * (str[i] - '0');
				t2 *= k;
			}

			if (isPrime(t1))
				break;

			A[k] = t1;
		}

		if (k > 10)	{
			j--;

			printf("%s ", str);
			
			for (i = 2; i <= 10; i++)	{
				if (A[i] % 2 == 0)
					printf("2 ");
				else
				{
					for (k = 3; k * k <= A[i]; k += 2)	{
						if (A[i] % k == 0)	{
							printf("%lld ", k);
							break;
						}
					}
				}
			}

			printf("\n");
		}

		return;
	}
	else
	{
		str[a] = '0';
		rec(a + 1);
		str[a] = '1';
		rec(a + 1);
	}
}

int main(void)	{
	int test, T;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);

	for (test = 1; test <= T; test++)	{
		scanf("%d%d", &n, &j);

		printf("Case #%d:\n", test);

		str[0] = str[n - 1] = '1';
		str[n] = 0;
		rec(1);
	}

	return 0;
}