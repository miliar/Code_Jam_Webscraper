#include <iostream>
#include <cstdio>

using namespace std;
typedef long double LD;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int T, it = 0;
	cin >> T;
	cout.precision(7);
	cout << fixed;
	while (T--) {

		++it;
		cout << "Case #" << it << ": ";

		LD c, f, x, ans = 1e100, t = 0;
		cin >> c >> f >> x;
		for (int i = 0; ; ++i) {
			LD a = t + x / (2 + i * f);
			if (a > ans) break;
			ans = a;
			t += c / (2 + i * f);
		}

		cout << (double)ans << endl;
	}

	return 0;
}
