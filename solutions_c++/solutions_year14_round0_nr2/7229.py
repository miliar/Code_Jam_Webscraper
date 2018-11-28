#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"
#include "iomanip"

using namespace std;

double solve(double c, double f, double x) {
	int n = max(floor(x / c - 2.0 / f), 0.0);
	double s = 0, a, b;
	a = x / (2 + n*f);
	for (int i = n-1; i >= 0; --i) {
		b = c / (2 + i*f);
		if (a > 0 && a < b) {
			s += a;
			a = -1;
		}
		s += b;
	}
	if (a > 0) s += a;
	return s;
}

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		double c, f, x;
		cin >> c >> f >> x;
		cout << "Case #" << t << ": " << fixed << setprecision(7) << solve(c, f, x) << endl;
	}
	
	return 0;
}
