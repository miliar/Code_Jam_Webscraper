#include <stdio.h>

int T;
double c, f, x, tmin;

int main() {
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);

	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		
		double ti1 = 0, tfinish;
		double tmin = x;

		for (int i = 0; i <= x; i++) { // number of farms
			// ti1 = timpul de costructie al fermei i-1
			tfinish = ti1 + x / (2 + i * f);
			if (tmin > tfinish) {
				tmin = tfinish;
			}
			ti1 = ti1 + c / (2 + i * f);
		}

		printf("Case #%d: %.7lf\n", t, tmin);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
