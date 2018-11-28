#include <stdio.h>

int main()
{
	int T;
	double C, F, X;
	double min = 0.0;
	double tt;
	int xh = 0;
	scanf("%d", &T);
	while (T-- > 0)
	{
		double ago = 0.0, tt = 0.0, rate = 2.0;


		scanf("%lf %lf %lf", &C, &F, &X);
		if (X <= C)
		{
			min = X / rate;
			printf("Case #%d: %.7lf\n", ++xh, min);
			continue;
		}
		else
		{
			min = X / rate;
		}
		do 
		{
			
			ago = min;
			//ago = X / 2.0;
			
			tt = tt + C / rate;
			rate = F + rate;
			min = tt + X / rate;
		} while (min < ago);

		printf("Case #%d: %.7lf\n", ++xh, ago);

	}
	return 0;
}