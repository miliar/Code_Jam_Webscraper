#include <cstdio>
const double eps = 1e-8;
int main() {
	int testnum;
	double C, F, X;
	scanf("%d", &testnum);
	for (int test = 1;test <= testnum;test++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: ", test);
		if (X <= C + eps) {
			printf("%.7lf\n", X * .5);
		} else {
			int low = int(X / C - 2.0 / F) - 3;
			if (low < 0) low = 0;
			double ans = -1;
			for (int i = low;i < low + 7;i++) {
				double tmp = 0;
				for (int j = 0;j < i;j++) {
					tmp += 1.0 / (2.0 + j * F);
				}
				tmp *= C;
				tmp += X / (2.0 + i * F);
				if (ans < 0 || tmp < ans) ans = tmp;
			}
			printf("%.7lf\n", ans);
		}
	}
	return 0;
}
