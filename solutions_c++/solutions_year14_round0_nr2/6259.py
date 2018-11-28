#include <cstdio>

int main () {
	int T;
	scanf("%d",&T);
	double C, F, X;
	for (int t = 0; t < T; t++) {
		scanf("%lf %lf %lf;f", &C, &F, &X);
		// printf("%f %f %f\n",C,F,X);
		double r = 2;
		double tim = 0;
		while (true) {
			double farmCost = C/r;
			double nextCookieCost = farmCost + X/(r+F);
			double cookieCost = X/r;
			// printf("Farm = %f, Cookie = %f, r = %f\n",farmCost,cookieCost,r);
			if (nextCookieCost < cookieCost) {
				// printf("  Farm < cookie\n");
				tim += farmCost;
				r += F;
				// break;
			} else {
				// printf("  Farm >= cookie\n");
				tim += cookieCost;
				break;
			}
		}
		printf("Case #%d: %.7f\n", t+1, tim);
	}


	return 0;
}