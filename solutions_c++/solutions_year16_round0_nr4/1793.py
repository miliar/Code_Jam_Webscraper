#include <bits/stdc++.h>
using namespace std;

void solve() {
	long long k, c, s;
	cin >> k >> c >> s;
	long long x = 1;
	for (long long i = 0; i < c; ++i) {
		x *= k;
	}
	for (long long i = 1; i <= k; ++i) {
		cout << (x / k) * i << ' ';
	}
	cout << endl;
	return;
}

int main() {
	long long T;
	cin >> T;
	for (long long t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
}
