#include <stdio.h>
#include <stdlib.h>
bool viz[10];
void init()
{
	int i;
	for (i = 0; i < 10; i++)
	{
		viz[i] = false;
	}
}
void cifre(long long n)
{
	while (n != 0)
	{
		viz[n % 10] = true;
		n = n / 10;
	}
}
bool verif()
{
	int i;
	for (i = 0; i < 10; i++)
	{
		if (viz[i] == false)
		{
			return false;
		}
	}
	return true;
}
long long solve(long long n)
{
	if (n == 0)
	{
		return 0;
	}
	long long i = 2, x = n, nr = 0;
	while (verif() == false)
	{
		cifre(n);
		n = i*x;
		i++;
	}

	return (n - x);
}
int main()
{
	FILE *f = fopen("fis.in", "r");
	FILE *g = fopen("fis.out", "w");
	long long t, n, ind = 1;
	fscanf(f, "%lld", &t);
	while (t--)
	{
		fprintf(g, "Case #%d: ", ind);
		init();
		fscanf(f, "%lld", &n);
		long long rez = solve(n);
		if (rez == 0)
		{
			fprintf(g, "INSOMNIA\n");
		}
		else
		{
			fprintf(g, "%lld\n", rez);
		}
		ind++;
	}
}