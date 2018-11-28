#include <cstdio>
#include <cstring>

int main() {
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double ans = X / 2.0, es = 0;
		for (int i = 0; ; i++) {
			double t = es + C / (2 + i*F) + X / (2 + i*F + F);
			if (ans < t) {
				break;
			} else {
				ans = t;
			}
			es += C / (2 + i*F);
		}
		printf("Case #%d: %.7lf\n", ca, ans);
	}
	return 0;
}
