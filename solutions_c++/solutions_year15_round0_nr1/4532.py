#include <stdio.h>

int main()
{
	int t, i;

	FILE *fin, *fout;
	fin= fopen("input.txt", "r");
	fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &t);
	for (i = 1; i <= t; i++)
	{
		int n, j, a, sum = 0, max=0;

		fscanf(fin, "%d", &n);
		for (j = 1; j <= n + 1; j++)
		{
			fscanf(fin, "%1d", &a);
			sum += a;
			if (j - sum > max) max = j - sum;
		}
		fprintf(fout, "Case #%d: %d\n", i, max);
	}
	return 0;
	
}