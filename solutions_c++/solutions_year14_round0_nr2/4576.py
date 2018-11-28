#include <cstdio>

int main()
{
	FILE *f;
	f = fopen("test.out", "w");
	freopen("B-large.in", "r", stdin);
	int n;
	double C, F, X, S, time;
	scanf("%d", &n);
	for (int N=1;N<=n;N++)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		time = 0.0;
		S = 2.0;
		while (X/S > C/S + X/(S+F))
		{
			time += C/S;
			S += F;
		}
		time += X/S;
		fprintf(f, "Case #%d: %f\n", N, time);
	}
	fclose(f);
	return 0;
}
