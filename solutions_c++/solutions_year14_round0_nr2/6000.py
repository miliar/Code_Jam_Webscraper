#include <cstdio>
#include <algorithm>
using namespace std;

double C, F, X;

double f(int k) {
	double ret = 0, v = 2;
	for (int i=0; i<k; v+=F,++i) ret += 1.0 / v;
	ret *= C;
	return ret;
}

int main() {
	int tc, cn = 0;
	for (scanf("%d", &tc); tc--; ) {
		scanf("%lf%lf%lf", &C, &F, &X);
		int k = X / C - 2 / F - 1;
		double t = f(k), v = 2 + max(0, k) * F, mn = t + X / v;
		for (int i=0; i<5; ++i) {
			t += C / v;
			v += F;
			mn = min(mn, t+X/v);
		}
		printf("Case #%d: %.7lf\n", ++cn, mn);
	}
	return 0;
}
