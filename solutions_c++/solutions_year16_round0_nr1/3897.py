#include <stdio.h>

int main()
{
	int ii, test, n, i, j, list[10], ans;
	FILE *fp_r, *fp_w;
	fp_w = fopen("output.txt", "w");
	fp_r = fopen("A-large.in", "r");


	fscanf(fp_r, "%d", &test);
	for (ii = 1;ii <= test;ii++)
	{
		fprintf(fp_w, "CASE #%d: ", ii);
		fscanf(fp_r, "%d", &n);
		if (n == 0)
		{
			fprintf(fp_w, "INSOMNIA\n");
			continue;
		}
		ans = 0;
		for (i = 0;i < 10;i++)
			list[i] = 0;
		while (1)
		{
			for (i = 0;i < 10;i++)
				if (list[i] == 0)
					break;
			if (i == 10)
			{
				fprintf(fp_w, "%d\n", ans*n);
				break;
			}
			j = (ans + 1)*n;
			while (j > 0)
			{
				list[j % 10] = 1;
				j /= 10;
			}
			ans++;
		}
	}



	fclose(fp_w);
	fclose(fp_r);
	return 0;
}