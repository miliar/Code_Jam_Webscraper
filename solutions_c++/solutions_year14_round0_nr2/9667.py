#include <cstdio>
#include <cmath>

int main()
{
	int T;
	double C,F,X, wyn, tmp;
	double tab[2001];
	scanf("%d\n", &T);
	for(int i = 1; i<= T; i++)
	{
		scanf("%lf %lf %lf", &C, &F, &X);
		double start = 2.0;
		
		for(int j = 0 ;j<X; j++)
		{
			tab[j] = C/start;
			start += F;
		}

		double mini = X / 2;

		tmp = 0.0;

		start = 2.0 + F;

		for(int j = 0; j < X; j++)
		{
			tmp += tab[j];
			mini = fmin(mini, tmp + X/start);
			start += F;
		}

		printf("Case #%d: %lf\n", i, mini);
	}
	return 0;
}