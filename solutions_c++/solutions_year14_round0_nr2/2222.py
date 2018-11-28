#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

const int PROD = 2;

FILE *f = fopen("input.in", "r");
FILE *g = fopen("output.out", "w");

int T;
double C, F, X;

int main()
{
	fscanf(f, "%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		fscanf(f, "%lf %lf %lf", &C, &F, &X);
		double prod = PROD;
		double t_min = X / prod;
		/*double t_int = 0;
		while (prod < X && t_int < t_min)
		{
			t_int = t_int + C / prod;
			prod = prod + F;
			if (t_min > t_int + X / prod)
			{
				t_min = t_int + X / prod;
			}
		}*/
		double t_int = C / prod;
		prod = prod + F;
		while (t_min > t_int + X / prod)
		{
			t_min = t_int + X / prod;
			t_int = t_int + C / prod;
			prod = prod + F;
		}
		fprintf(g, "Case #%d: %.7lf\n", t, t_min);
	}

	fclose(f);
	fclose(g);
}