#include <cstdio>
#include <math.h>

#define LOCAL_DEBUG

using namespace std;

double C, F, X;

double solve() {
	double rate = 2.0;
	double minTime = X/rate;
	double buildTime = 0.0;
	while (1) {
		if (buildTime > minTime)
			break;
		// Build
		buildTime += C/rate;
		rate += F;
		double expectedTime = buildTime + X/rate; 
		minTime = fmin(minTime, expectedTime);
	}
	return minTime;
}

int main() {
#ifdef LOCAL_DEBUG
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		double ans = solve();
		printf("Case #%d: %.7lf\n", t, ans);
	}
	return 0;
}