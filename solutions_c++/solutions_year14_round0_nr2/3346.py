#include <stdio.h>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);

		double best = 1e100;

		double cur = 0;
		int farms = 0;
		while (cur < best) {
			best = min(best, cur + X / (2 + F * farms));
			cur += C / (2 + F * farms);
			farms++;
		}
		printf("Case #%d: %.8lf\n", ca, best);
	}
	return 0;
}