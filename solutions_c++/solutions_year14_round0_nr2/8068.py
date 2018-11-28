#include <stdio.h>

int main () {
	int t,count = 1;
	double c,f,x, rate,ti;
	scanf("%d", &t);
	while(t--) {
		scanf("%lf %lf %lf", &c, &f, &x);
		rate = 2; ti = 0;

		while( x/rate > c/(rate) + x/(rate+f)) {
			ti += c/rate;
			rate += f;
		}
		ti += x/rate;
		printf("Case #%d: %.7lf\n",count++, ti);
	}
	return 0;
}