#include <iostream>
#include <iomanip>
using namespace std;

typedef long double ld;

int main() {
	int nt, it;

	cin >> nt;

	for (it = 1; it <= nt; it++) {
		ld c, f, x;
		ld t = 0, r = 1E9;
		int i;

		cin >> c >> f >> x;
		for (i = 0; i < 1000000; i++) {
			r = min(r, t + x / (i * f + 2));
			t += c / (i * f + 2);
		}

		cout << "Case #" << it << ": " << setprecision(10) << fixed << r << '\n';
	}
}
