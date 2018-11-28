#include <cstdio>

int main(void) {
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		double c = 0, f = 0, x = 0, t = 0;
		double rate = 2;
		bool ok = true;
		scanf("%lf%lf%lf", &c, &f, &x);
		while (ok) { //on a toujours 0 cookies en fait
			double tsans = x/rate;
			double touvrir = c/rate;
			double tavec = x/(rate+f);
			if (touvrir+tavec < tsans) {
				t += touvrir;
				rate += f;
			} else {
				ok = false;
				t += tsans;
			}
		}
		printf("Case #%d: %lf\n", test, t);
	}
	return 0;
}	
