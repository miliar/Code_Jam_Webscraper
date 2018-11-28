#include <cstdio>

#define EPS 1e-8

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);
		double answ = 0.0;
		double speed = 2.0;
		double goingThrough, buildAndGoThrough;
		do {
			goingThrough = X / speed;
			buildAndGoThrough = C / speed + X / (speed + F);
			if (goingThrough > buildAndGoThrough) {
				answ += C / speed;
				speed += F;
			}
		} while (goingThrough > buildAndGoThrough);
		answ += goingThrough;
		printf("Case #%d: %.8lf\n", t, answ);
	}
	return 0;
}