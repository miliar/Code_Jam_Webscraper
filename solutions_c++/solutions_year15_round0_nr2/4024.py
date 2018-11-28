#include <stdio.h>

FILE *fin, *fout;

int F(int n, int k)
{
	if (n <= k) return 0;

	int min=10000000, i;
	int a, b;

	for (i = 1; i <= (n/2); i++)
	{
		a = F(n - i, k);
		b = F(i, k);
		if (min > a + b + 1) min = a + b + 1;
	}
	return min;
}

int main()
{
	int t, i, j, k;

	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &t);
	for (i = 1; i <= t; i++)
	{
		int n, cnt[1001] = { 0, };
		int a;
		int sum=0, ans=10000000, cut=0;

		fscanf(fin, "%d", &n);
		for (j = 0; j < n; j++)
		{
			fscanf(fin, "%d", &cnt[j]);
			if (cut < cnt[j]) cut = cnt[j];
		}

		for (j = 1; j <= cut; j++)
		{
			sum = 0;
			for (k = 0; k < n; k++)
			{
				sum+=F(cnt[k], j);
			}
			if (sum + j < ans) ans = sum + j;
		}
		fprintf(fout, "Case #%d: %d\n", i, ans);
	}
	fclose(fin);
	fclose(fout);

	return 0;
}