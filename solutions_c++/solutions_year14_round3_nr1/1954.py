#include<stdio.h>
int main(void)
{
	int T, count;
	int P, Q;
	char buffer;
	double tmp;
	FILE *fp, *fp2;
	fp = fopen("A-small-attempt0.in", "rt");
	fp2 = fopen("output.txt", "wt");
	fscanf(fp, "%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int j;
		fscanf(fp, "%d", &P);
		fscanf(fp, "%c", &buffer);
		fscanf(fp, "%d", &Q);
		count = 0;
		for (j = 0; j<40; j++)
		{
			tmp = (double)P / (double)Q;
			if (tmp > 0.5)
			{
				P *= 2;
				P -= Q;
				if (count == 0)
					count = j + 1;
			}
			else if (tmp == 0.5)
			{
				if (count == 0)
					count = j + 1;
				break;
			}
			else
			{
				P *= 2;
			}
		}
		if (j > 39)
		{
			fprintf(fp2, "Case #%d: impossible\n", i);
		}
		else
		{
			fprintf(fp2, "Case #%d: %d\n", i, count);
		}
	}
	fclose(fp);
	fclose(fp2);

	return 0;
}