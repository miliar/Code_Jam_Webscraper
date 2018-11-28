#include <stdio.h>
#include <stdlib.h>
int a[35], J, nr;
void genereaza()
{
	int n = J - 2, carry = 1;
	while (true)
	{
		a[n] = a[n] + carry;
		if (a[n] == 2)
		{
			a[n] = 0;
			carry = 1;
		}
		else
		{
			carry = 0;
		}
		if (carry == 0 || n == 1)
		{
			break;
		}
		n--;
	}
}
long long transorm(int base)
{
	long long sum = 0, p = 1;
	int i;
	for (i = J - 1; i >= 0; i--)
	{
		sum = sum + p*a[i];
		p = p*base;
	}
	return sum;
}
long long prime(long long x)
{
	long long k = 2;
	if (x == 2 || x == 3)
	{
		return 0;
	}
	while ((k*k) <= x)
	{
		if (x%k == 0)
		{
			return k;
		}
		k++;
	}
	return 0;
}
int main()
{
	FILE *f = fopen("fis.in", "r");
	FILE *g = fopen("fis.out", "w");
	int t;
	fscanf(f, "%d", &t);
	fscanf(f, "%d %d", &J, &nr);
	fprintf(g, "Case #1:\n");
	a[0] = a[J - 1] = 1;
	while (nr != 0)
	{
		int base, cnt = 0, i;
		long long div[12];
		for (base = 2; base <= 10; base++)
		{
			long long ans = transorm(base);
			div[cnt] = prime(ans);
			if (div[cnt] == 0)
			{
				break;
			}
			cnt++;
		}
		if (base == 11)
		{
			for (i = 0; i < J; i++)
			{
				fprintf(g, "%d", a[i]);
			}
			fprintf(g, " ");
			for (i = 0; i < cnt; i++)
			{
				fprintf(g, "%d ", div[i]);
			}
			fprintf(g, "\n");
			nr--;
		}

		genereaza();
	}
}