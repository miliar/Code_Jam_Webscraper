#include <bits/stdc++.h>

using namespace std;

typedef __int128 ll;

#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

const double EPS = 1e-9;
const ll INF = 1e17;

ll findDivisor(ll num) {
	for (ll i = 2; i * i <= num && i <= 1e6; i++) {
		if (num % i == 0) return i;
	}

	return 0;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(nullptr);
	cout.tie(nullptr);

	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);

	int t;
	cin >> t;

	cout << "Case #1:\n";

	int n, j, cnt;
	cin >> n >> j;

	for (int i = 0; i < (1 << (n - 2)) && j; i++, cnt++) {
		ll mask = (1ll << (n - 1)) | ((ll)i << 1) | 1;
		vector<long long> divs;

		for (int base = 2; base <= 10; base++) {
			ll nowBase = 1, num = 0;

			for (int j = 0; j < n; j++) {
				num += nowBase * ((mask >> j) & 1ll);
				nowBase *= base;
			}

			ll divisor = findDivisor(num);

			if (divisor) {
				divs.push_back(divisor);
			}
		}

		if ((int)divs.size() == 9) {
			for (int j = n - 1; j >= 0; j--) {
				cout << (int)((mask >> j) & 1);
			}
			cout << " ";

			for (auto divisor : divs) {
				cout << divisor << " ";
			}
			cout << "\n";

			j--;

			cerr << j << "\n";
		}

		if (cnt == 1000) {
			cerr << "Another 1000, now: " << i << ", last: " << (1 << (n - 2)) - i << "\n";
			cnt = 0;
		}
	}

	return 0;
}
