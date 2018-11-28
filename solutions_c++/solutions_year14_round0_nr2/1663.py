#include <iostream>
#include <iomanip>

using namespace std;

bool doClick(long double s, long double f, long double c, long double x, long double &tp) {
	// don't buy farm
	long double ti = x / s;

	// buy farm
	long double tb = x / (s + f) + c / s;

	if (ti > tb) {
		tp += c / s;
	} else {
		tp += ti;
	}

	return tb < ti ? true : false;
}

int main() {
	int t = 0;
	long double c, f, x, s = 2.0;
	long double tp;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> c >> f >> x;
		//cout << c << ":" << f << ":" << x << endl;
		//
		tp = 0.0;
		s = 2.0;
		while (doClick(s, f, c, x, tp)) {
			s += f;
		}
		cout << setiosflags(ios::fixed | ios::showpoint) << setprecision(7) << "Case #" << i + 1 << ": " << tp << endl;
	}
	return 0;
}