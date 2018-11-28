#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define sz(x) ((int)(x).size())

ll fastPow(int a, int b) {
	ll ret = 1;
	for (int i = 0; i < b; ++i) {
		ret *= a;
	}
	return ret;
}

int main() {
	int test;
	cin >> test;
	for (int test_case = 1; test_case <= test; ++test_case) {
		cout << "Case #" << test_case << ": ";
		int k, c, s;
		cin >> k >> c >> s;
		int needed = k / c;
		if (needed * c != k) needed++;
		if (needed > s) cout << "IMPOSSIBLE" << endl;
		else {
			// ll a = 0;
			// for (int i = 0; c - i - 1 >= 0 && i + 1 < k; ++i) {
			// 	a += i * fastPow(k, c - i - 1);
			// }
			// for (int i = 0; i < needed; ++i) {
			// 	if (i != 0) cout << ' ';
			// 	cout << i * fastPow(k, c - 1) * c + a + 1;
			// }
			// cout << endl;
			for (int i = 0; i < k; ++i) {
				if (i != 0) cout << ' ';
				cout << i * fastPow(k, c - 1) + 1;
			}
			cout << endl;
		}
	}
	return 0;
}
