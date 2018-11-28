#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

bool VerifyPrim(char *buffer, int base, int a[])
{
	long long nr = 0;
	long long lbase = 1;

	for (int i = strlen(buffer) - 1; i >= 0; --i)
	{
		if (buffer[i] == '1')
		{
			nr = nr + lbase;
		}
		lbase = lbase * base;
	}

	for (int i = 2; i < 5000 && i < nr / 2; i += 2)
	{
		if (nr%i == 0)
		{
			a[base] = i;
			return false;
		}
		if (i == 2)
		{
			i = 3;
		}
	}

	return true;
}

int main()
{
	int t, n, k;
	int a[11];

	unsigned int move;
	char buffer[40];
	bool ok;

	FILE *fin, *fout;

	fin = fopen("input3.in", "r");
	fout = fopen("output3.out", "w");

	fscanf(fin, "%d %d %d", &t, &n, &k);

	move = (1 << (n - 1)) + 1;

	fprintf(fout, "Case #1:\n");

	while (move < INT_MAX)
	{
		ok = true;
		memset(a, 0, 10 * sizeof(int));

		itoa(move, buffer, 2);
		for (int i = 2; i <= 10; ++i)
		{
			if (VerifyPrim(buffer,i,a) == true)
			{
				ok = false;
				break;
			}
		}

		if (ok == true)
		{
			k--;

			fprintf(fout, "%s ", buffer);
			for (int i = 2; i <= 10; ++i)
			{
				fprintf(fout, "%d ", a[i]);
			}
			fprintf(fout, "\n");
			
			if (k == 0)
			{
				break;
			}
		}

		move = move + 2;
	}


	fclose(fin);
	fclose(fout);
	return 0;
}