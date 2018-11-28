#include <cstdio>

void Solve() {
	double C, F, X;
	scanf("%lf %lf %lf", &C, &F, &X);
	double best = X / 2;
	double currTime = 0;
	for (int i = 0; currTime < best; i++) {
		double leftTime = X / (2 + F * i);
		if (currTime + leftTime < best)
			best = currTime + leftTime;
		currTime += C / (2 + F * i);
	}
	printf("%.10lf\n", best);
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		Solve();
	}
	return 0;
}
