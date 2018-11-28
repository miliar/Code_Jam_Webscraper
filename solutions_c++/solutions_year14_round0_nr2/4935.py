#include <cstdio>

int main(int argc, char const *argv[])
{
	int T;

	scanf("%d", &T);

	for (int k = 0; k < T; ++k)
	{
		double C, F, X;

		scanf("%lf %lf %lf", &C, &F, &X);

		double N = 2.0;

		double timepast=0;

		double dif = X-C;

		while ( (N*X) < (N+F)*dif )
		{
			timepast += (C/N);
			N += F;
		}

		timepast += X/N;

		printf("Case #%d: %.7lf\n", k+1, timepast);
	}
	return 0;
}