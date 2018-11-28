#include <cstdio>

int main()
{
	int tn, ti = 0;
	scanf("%d", &tn);
	while(tn--)
	{
		double C, F, X, V = 2, T = 0;
		scanf("%lf %lf %lf", &C, &F, &X);
		while(1)
		{
			if(X/V > C/V + X/(V+F)) 
			{
				T += C/V;
				V += F;
			}
			else
			{
				T += X/V;
				break;
			}
		}
		printf("Case #%d: %.7lf\n", ++ti, T);

	}
}

