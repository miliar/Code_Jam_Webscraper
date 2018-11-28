#include <iostream>

using namespace std;

int main() {
	int test_cases;

	double C, F, X, R, S;

	cin >> test_cases;
	cout.setf(std::ios_base::fixed, std::ios_base::floatfield);
	cout.precision(7);
	for (int kase = 1; kase <= test_cases; ++kase) {
		cout << "Case #" << kase << ": ";
		cin >> C >> F >> X;
		R = 2, S = 0;

		while (X / R > (C / R + X / (R + F)))
			S += C / R, R += F;
		cout << S + X / R << "\n";
	}

	return 0;
}