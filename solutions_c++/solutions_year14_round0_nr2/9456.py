#include <stdio.h>
#define eps 1e-8
int dcmp(double x) {
	return (x > eps) - (x < -eps);
}
int main()
{
	int T;
	scanf("%d", &T);
	int icase = 0;
	while (T--) {
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double now = 0.0;
		double rate = 2.0;
		bool flag = true;
		while (flag) {
			if (dcmp(X/rate-(X/(rate+F)+C/rate)) <= 0) {
				flag = false;
				now += X / rate;
			} else {
				now += C / rate;
				rate += F;
			}
		}
		++icase;
		printf("Case #%d: %.7lf\n", icase, now);
	}
	return 0;
}
