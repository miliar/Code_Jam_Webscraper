#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;

	cout << fixed;
	cout.precision(7);

	for (int test = 1; test <= t; test++) {
		double c, f, x;
		cin >> c >> f >> x;

		double farm_buying_time = 0;
		double prev_ans = x / 2;

		for (int i = 1;; i++) {
			farm_buying_time += c / (2 + (i - 1) * f);
			double ans = x / (2 + i * f) + farm_buying_time;

			if (ans > prev_ans) {
				cout << "Case #" << test << ": " << prev_ans << endl;
				break;
			}

			prev_ans = ans;
		}
	}
}