#include<stdio.h>
int main(void)
{
	int T, next;
	double C, F, X, min, now, tmp;
	FILE *fp, *fp2;
	fp = fopen("B-large.in", "rt");
	fp2 = fopen("output.txt", "wt");
	fscanf(fp, "%d", &T);
	for (int i = 0; i < T; i++)
	{
		fscanf(fp, "%lf %lf %lf", &C, &F, &X);
		next = 1;
		min = X / 2;
		now = 1.0 / 2;
		tmp = (X / (2 + next*F)) + (C * now);
		while (tmp < min)
		{
			min = tmp;
			now = now + (1 / (2 + next*F));
			next++;
			tmp = (X / (2 + next*F)) + (C * now);
		}
		fprintf(fp2, "Case #%d: %.7lf\n", i + 1, min);
	}
	fclose(fp);
	fclose(fp2);

	return 0;
}