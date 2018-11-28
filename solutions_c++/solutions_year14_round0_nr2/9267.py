#include <cstdio>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);

	for (int caseNum = 1; caseNum <= t; caseNum++) {
		printf("Case #%d: ", caseNum);

		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		double prod = 2;
		double best = X / prod;
		double next = 0;

		while (true) {
			next += C / prod;
			prod += F;
			if (best > next + (X / prod)) {
				best = next + X / prod;
			}
			else {
				break;
			}
		}
		printf("%.7f\n", best);
	}
}

