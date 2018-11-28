#include <iostream>
#include <math.h>
using namespace std;

const double EPSILON = 0.000001;

bool equal(double a, double b) {
	return fabs(a - b) < EPSILON;
}

int main() {
	int testCases;
	cin >> testCases;

	cout.setf(ios::fixed);
	cout.setf(ios::showpoint);
	cout.precision(7);

	for (int testCase = 1; testCase <= testCases; ++testCase) {
		double minSecReq = numeric_limits<double>::max();

		double C, F, X;
		cin >> C >> F >> X;

		for (int i = 0; true; ++i) {
			double secReq = X / (2.0 + i*F);

			for (int j = 0; j < i; ++j) {
				secReq += C / (2.0 + j*F);
			}

			if (secReq < minSecReq) {
				minSecReq = secReq;
			}
			else {
				break;
			}
		}

		cout << "Case #" << testCase << ": " << minSecReq << endl;
	}

	return 0;
}
