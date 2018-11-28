#include <stdio.h>
#include <stdlib.h>
using namespace std;

const int INIT_RATE = 2;
const int LOWER = 0;
const int UPPER = 100000;
const double EPS = 1e-8;

double check_time(int farms, double C, double F, double X) {
	double rate = INIT_RATE;
	double sol = 0.;
	int bought = 0;

	while (bought < farms) {
		sol += C/rate;
		rate += F;
		bought++;
	}

	sol += X / rate;
	return sol;
}

double ternary_search(double C, double F, double X) {
	int left, right;
	int left_mid, right_mid;

	left = LOWER;
	right = UPPER;
	double sol_left = 0;
	double sol_right = 0;

	while(right - left > 1) {
		// printf("LEFT: %d RIGHT: %d\n", left, right);
		left_mid = (left * 2 + right)/3;
		right_mid = (left + 2* right)/3;

		if (check_time(left_mid, C, F, X) - check_time(right_mid, C, F, X) < 0.) {
			right = right_mid-1;
		} else {
			left = left_mid+1;
		}
	}

	sol_left = check_time(left, C, F, X);
	sol_right = check_time(right, C, F, X);
	return sol_left < sol_right ? sol_left : sol_right;
}

int main(void) {
	double C, F, X;
	int T;
	int counter = 1;
	scanf("%d", &T);

	while(counter <= T) {
		scanf("%lf %lf %lf", &C, &F, &X);
		printf("Case #%d: ", counter);
		printf("%.7lf\n", ternary_search(C, F, X));
		counter++;
	}

	return 0;
}