#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;
typedef long long ll;

ll run(ll N) {
	bool filled = false;
	bool digits[10];
	fill(digits, digits + 10, false);
	ll A = 0;
	while (!filled) {
		A += N;
		ll k = A;
		while (k > 0) {
			digits[k % 10] = true;
			k /= 10;
		}
		filled = true;
		for (int i = 0; i < 10; ++i) {
			if (!digits[i]) {
				filled = false;
				break;
			}
		}
	}
	return A;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; cin >> T;
	for (int t = 0; t < T; ++t) {
		int N; cin >> N;
		cout << "Case #" << (t + 1) << ": ";
		if (N == 0) cout << "INSOMNIA";
		else cout << run(N);
		cout << endl;
	}
}