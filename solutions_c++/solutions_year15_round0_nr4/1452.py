#include<iostream>
#include<string>
using namespace std;

int main() {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int t, it, x, r, c;
	bool gabriel;
	cin >> t;
	for (it = 1; it <= t; it++) {
		cin >> x >> r >> c;
		gabriel = false;
		if (x == 1) {
			gabriel = true;
		}
		if (x == 2 && (r % 2 == 0 || c % 2 == 0)) {
			gabriel = true;
		}
		if (x == 3 && ((r % 3 == 0 && c > 1) || (c % 3 == 0 && r > 1))) {
			gabriel = true;
		}
		if (x == 4 && ((r == 4 && c == 4) || (r == 3 && c == 4) || (r == 4 && c == 3))) {
			gabriel = true;
		}
		if (gabriel) {
			cout << "Case #" << it << ": GABRIEL\n";
		} else {
			cout << "Case #" << it << ": RICHARD\n";
		}
	}
	return 0;
}