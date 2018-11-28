#include <stdio.h>

int main()
{
	int n;
	int son[1000], mom[1000];
	char trash[1000];
	int i, j;
	int t, r;
	int cnt1, cnt2;

	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");

	fscanf(fin, "%d", &n);
	for (i = 0; i < n; i++)
	{
		fscanf(fin, "%d", &son[i]);
		fscanf(fin, "%c", &trash[i]);
		fscanf(fin, "%d", &mom[i]);
	}

	for (i = 0; i < n; i++)
	{	
		for (j = 2; j*j <= mom[i]; j++)
		{
			if (mom[j] % j == 0 && son[j] % j == 0)
			{
				mom[j] /= j;
				son[j] /= j;
				j--;
			}
		}

		t = mom[i]; r = 1; cnt1 = 0;
		while (t != 1)
		{
			t /= 2;
			r *= 2;
			cnt1++;
		}
		if (mom[i] != r)
		{
			fprintf(fout, "Case #%d: Impossible\n", i+1);
			continue;
		}
		son[i] *= 2; r = 1; cnt2 = -1;
		while (r <= son[i])
		{
			r *= 2;
			cnt2++;
		}

		fprintf(fout, "Case #%d: %d\n", i+1, cnt1 - cnt2+1);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}