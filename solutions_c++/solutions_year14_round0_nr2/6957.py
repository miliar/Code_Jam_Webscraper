#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

#define TEST_CASE "B-large"
#define I 2.0

double solve(double C, double F, double X) {
	double res = 0, i = I;
	int fc = 0;
	while (true) {
		double next_farm_in = C / (fc * F + I);
		double all_in = X / (fc * F + I);
		double all_with_next_farm = X / (fc * F + F + I);
		if (next_farm_in + all_with_next_farm < all_in) {
			res += next_farm_in;
			fc++;
		} else {
			res += all_in;
			break;
		}
	}

	return res;
}

int main() {
	int T;

	fstream cin(TEST_CASE ".in");
	ofstream cout(TEST_CASE ".out");

	cin >> T;

	for(int t=0; t < T; t++) {
		double C, F, X;
		cin >> C >> F >> X;
		cout.precision(15);
		cout << "Case #" << t + 1 << ": " << fixed << solve(C, F, X) << endl;
	}
	
	return 0;
}