#include <bits/stdc++.h>
using namespace std;

void update(long long x, set <int> &digits) {
	while (x > 0) {
		digits.erase(x % 10);
		x /= 10;
	}
	return;
}

void solve() {
	long long n;
	cin >> n;
	set <int> digits;
	for (int i = 0; i < 10; ++i) {
		digits.insert(i);
	}
	for (int i = 1; i < (int)1e6; ++i) {
		update(i * n, digits);
		if (digits.empty()) {
			cout << i * n << endl;
			return;
		}
	}
	cout << "INSOMNIA" << endl;
	return;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
}