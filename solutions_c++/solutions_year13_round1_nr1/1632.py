#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int n_cases;
	cin >> n_cases;
	for (int cc = 1; cc <= n_cases; cc++) {
		long double r;
		long double t;
		cin >> r >> t;
		long double x = 0.25 * (sqrtl(4 * r * r - 4 * r + 8 * t + 1) - 2 * r + 1);
		int result = floor(x);
		cout << "Case #" << cc << ": " << result << endl;
	}
}
