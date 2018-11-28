#include <cstdio>
#include <cstring>

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++ cas) {
		double C, F, X, D = 2.0;
		scanf("%lf%lf%lf", &C, &F, &X);
		double ret = X / D, tmp = 0;
		while (1) {
			tmp += C / D;
			D += F;
			if (tmp + X / D < ret) {
				ret = tmp + X / D;
			}
			else break;
		}
		printf("Case #%d: %.7lf\n", cas, ret);
	}
	return 0;
}
