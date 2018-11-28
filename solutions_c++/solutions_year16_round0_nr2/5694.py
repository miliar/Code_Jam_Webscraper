#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int a[110], minim;

void flip(int k, int s)
{
	int b[110];
	for (int i = 1; i <= s; ++i)
	{
		b[i] = a[i];
	}
	for (int i = 1; i <= k; ++i)
	{
		a[i] = !b[k - i + 1];
	}
}

int main()
{
	int t, s;
	char str[110];
	bool ok;

	FILE *fin, *fout;

	fin = fopen("input2.in", "r");
	fout = fopen("output2.out", "w");

	fscanf(fin, "%d ", &t);

	for (int i = 1; i <= t; ++i)
	{
		printf("TEST %d\n", i);

		fscanf(fin, "%s", str);

		minim = 0;
		ok = true;

		for (int j = 0; j < strlen(str); ++j)
		{
			if (str[j] == '+')
			{
				a[j + 1] = 1;
			}
			else if (str[j] == '-')
			{
				ok = false;
				a[j + 1] = 0;
			}
		}

		s = strlen(str);

		if (!ok)
		{
			while (!ok)
			{
				ok = true;
				for (int j = 1; j < s; ++j)
				{
					if (a[j] != a[j + 1])
					{
						ok = false;
						minim += 1;
						flip(j, s);
					}
				}

				if (ok && a[s] == 0)
				{
					minim = minim + 1;
				}
			}
		}

		fprintf(fout, "Case #%d: %d\n", i, minim);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}