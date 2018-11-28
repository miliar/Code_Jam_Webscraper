#include <iostream>
#include <string>
#include <algorithm>
#define ll long long
using namespace std;

ll J, N;
ll mult[11][33];

void init() {
	int i, j;
	for (i = 2; i < 11; ++i) {
		mult[i][0] = 1;
		for (j = 1; j < 33; ++j) {
			mult[i][j] = mult[i][j - 1] * (ll) i;
		}
	}
}

ll check(ll num) {
	ll i;
	if (num < 4) {
		return 0;
	}
	if (num % 2 == 0) {
		return 2;
	}
	for (i = 3; i * i <= num; i += 2) {
		if (num % i == 0) {
			return i;
		}
	}
	return 0;
}

void solve() {
	cout << '\n';
	ll mask;
	ll cr;
	ll num;
	int i, base;
	int r, res[11];
	bool isOk;
	for (mask = ((1<<N) / 2 + 1); mask < (1<<N) && J > 0; mask += 2) {
		isOk = true;
		for (base = 2; base < 11 && isOk; ++base) {
			num = 0;
			for (i = 0; i < N; ++i) {
				if (mask & (1<<i)) {
					num += mult[base][i];
				}
			}
			//cout << mask << ' ' << base << ' ' << num << '\n';
			r = check(num);
			if (r == 0) {
				isOk = false;
			} else {
				res[base] = r;
			}
		}
		if (isOk) {
			for (i = N - 1; i >=0; --i) {
				cout << ((mask & (1<<i)) > 0) ? '1' : '0';
			}
			for (base = 2; base < 11; ++base) {
				cout << " " << res[base];
			}
			cout << '\n';
			--J;
		}
	}
}

int main() {
	init();
	int tc, T;
	cin >> T;
	for (tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ":";
		cin >> N >> J;
		solve();
	}
	return 0;
}