#include <stdio.h>

using namespace std;

int main() {
	int tests = 0;
	double C, F, X;
	double result = 0.0, rate = 0.0;

	if (scanf("%d\n", &tests) != 1) {
		fprintf(stderr, "Wrong input format\n");
	}	

	for (int i = 1; i <= tests; i++) {
		rate = 2.0;
		result = 0.0;
		if (scanf("%lf %lf %lf\n", &C, &F, &X) != 3) {
			fprintf(stderr, "Wrong input format\n");
		}
		
		while (true) {
			if ( ((X / rate) + result) < (X / (rate + F)) + result + C / rate) {
				result += X / rate;
				break;
			}
			result += C / rate;
			rate += F;
		}

		printf("Case #%d: %.7lf\n", i, result);
	}
	return 0;
}
