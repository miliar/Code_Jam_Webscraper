#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;



int main()
{
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("A-large.out", "w");
	int t;
	fscanf(in, "%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int n, s[1111] = { 0 };
		fscanf(in, "%d", &n);
		for (int j = 0; j <= n; j++)
		{
			fscanf(in, "%1d", &s[j]);
		}

		int sum = 0, frd = 0;
		for (int j = 0; j <= n; j++)
		{
			if (sum >= j)
			{
				sum += s[j];
			}
			else
			{
				frd += j - sum;
				sum += j - sum;
				sum += s[j];				
			}
		}


		fprintf(out, "Case #%d: %d\n", i, frd);
	}

	fclose(in);
	fclose(out);

	return 0;
}