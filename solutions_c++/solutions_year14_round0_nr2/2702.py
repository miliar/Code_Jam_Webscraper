#include<stdio.h>

int main()
{
	int T;
	int Case = 1;
	scanf("%d", &T);
	while ( T-- ) {
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double sum = 0.0;
		double rate = 2.0;
		for ( int i = 0 ; i <= X ; i++ ) {
			if ( C/rate + X/(rate+F) <= X/rate ) {
				sum += C/rate;
				rate += F;
			}
			else {
				sum += X/rate;
				break;
			}
		}
		printf("Case #%d: %6lf\n", Case++, sum);
	}
	
	return 0;
}
