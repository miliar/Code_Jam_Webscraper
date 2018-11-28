#include <iostream>
#include <iomanip>

using namespace std;

typedef long double ld;

int main() {
	int tt;
	cin >> tt;
	for (int o = 0; o < tt; o++) {
		ld c, f, x, cur = 2.0, pass = 0.0;
		cin >> c >> f >> x;
		ld best = x / cur;
		int last = -1;
		for (int i = 0; i < 10 * x + 1; i++) {
			pass += c / cur;
			cur += f;
			ld tmp = best;
			best = min(best, x / cur + pass);
			if (tmp > best)
				last = i;
		}
		cout << setprecision(10) << fixed << "Case #" << o + 1 << ": " << best << endl;
	}
	return 0;
}
