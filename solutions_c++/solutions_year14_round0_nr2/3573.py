#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cout << setprecision(10);
	cout << fixed;

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		double c, f, x;
		cin >> c >> f >> x;

		double t = c / 2, tmin = x / 2;
		int farms = 0;

		while (t < tmin) {
			farms++;
			tmin = min(tmin, t + x / (2 + farms * f));
			t += c / (2 + farms * f);
		}

		cout << "Case #" << tc << ": " << tmin << endl;
	}
	return 0;
}
