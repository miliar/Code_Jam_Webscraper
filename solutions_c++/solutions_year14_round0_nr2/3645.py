#include <cstdio>
#include <iostream>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	int i;

	for (i = 0; i < T; ++i) {
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		double time = 0;
		double gen = 2.0;

		int j;

		for (j = 0; j < 2000000; ++j) {
			if (X / gen >= (C / gen) + (X / (gen + F))) {
				time += C / gen;
				gen += F;
				continue;
			} else {
				time += X / gen;
				break;
			}
		}

		printf("Case #%d: %.7lf\n", i + 1, time);
	}

	return 0;
}