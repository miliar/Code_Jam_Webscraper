#include <iostream>

double C(0.0), F(0.0), X(0.0);

double S(int n) {
	double result = X / (2.0 + n * F);
	for (int i = 0; i < n; i++) {
		result += C / (2.0 + i * F);
	}
	return result;
}

int main() {
	using namespace std;
	int T(0), t(0), i(0);
	double best(0.0), current(0.0);

	cin >> T;
	cout.precision(7);
	cout << fixed;
	for (t = 1; t <= T; t++) {
		cin >> C >> F >> X;
		i = 0;
		best = S(i);
		while (1) {
			current = S(++i);
			if (current < best) {
				best = current;
			} else {
				break;
			}
		}
		cout << "Case #" << t << ": " << best << endl;
	}
}
