#include <cstdio>
using namespace std;
int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);
		double ans = 0, speed = 2;
		while (1) {
			if ((X-C)/speed <= X/(speed+F)) {
				ans += X/speed;
				break;
			} else {
				ans += C/speed;
				speed += F;
			}
		}
		printf("Case #%d: %.7lf\n", t, ans);
	}
	return 0;
}

