#include <iostream>
#include <stdio.h>

using namespace std;

void Decompose(long long aux ,bool a[])
{
	while (aux != 0)
	{
		a[aux % 10] = true;
		aux = aux / 10;
	}
}

long long DeterminValue(int n, bool a[])
{
	if (n <= 0)
	{
		return -1;
	}

	long long k = 0;
	bool find_all = false;
	do
	{
		k = k + 1;
		Decompose(k*n, a);

		find_all = true;
		for (int i = 0; i <= 9; ++i)
		{
			if (a[i] == false)
			{
				find_all = false;
				break;
			}
		}
	} while (find_all == false && 1LL*k*n < LLONG_MAX);
	if (find_all == false)
	{
		return -1;
	}
	return k*n;
}

int main()
{
	int t, n;
	long long out;
	bool a[10];

	FILE *fin, *fout;

	fin = fopen("input.in", "r");
	fout = fopen("output.out", "w");

	fscanf(fin, "%d", &t);

	for (int i = 1; i <= t; ++i)
	{
		fscanf(fin, "%d", &n);
		memset(a, false, 10 * sizeof(bool));
		out = DeterminValue(n, a);
		if (out == -1)
		{
			fprintf(fout, "Case #%d: INSOMNIA\n", i);
		}
		else fprintf(fout, "Case #%d: %lld\n", i, out);
	}


	fclose(fin);
	fclose(fout);
	return 0;
}