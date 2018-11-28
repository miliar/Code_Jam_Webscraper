#include<stdio.h>

using namespace std;

double rate = 2;
double time = 0;
double cks = 0;
double C, F, X;

#define NB  (X - cks)/rate

int main()
{
	int T,Case=1;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%lf %lf %lf",&C, &F, &X);
		rate = 2;
		time = 0;
		cks = 0;
		while(cks<X)
		{
			double tTB, tTBuy, nrate;
			tTBuy = C/rate;
			nrate = rate+F;
			tTB = tTBuy + ((X-cks)/nrate);
			if(NB < tTB)
			{
				time += (X - cks)/rate;
				cks = X;

			}
			else
			{
				time +=  C/rate;
				rate += F;
			}
		}
		printf("Case #%d: ", Case++);
		printf("%.8f\n", time);
	}
}


