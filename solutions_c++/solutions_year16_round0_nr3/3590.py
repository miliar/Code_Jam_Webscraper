#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
typedef long long ll;

ll translate10(int base, ll n) {
	ll ans = 0;
	int i = 0;
	while (n > 0) {
		ans += pow(base, i) * (n % 10);
		n /= 10;
		i++;
	}
	return ans;
}

ll translate2(ll n) {
	vector<int> v;
	while (n > 1) {
		v.push_back(n % 2);
		n /= 2;
	}
	v.push_back(n);
	ll ans = 0;
	for (int i = v.size() - 1; i >= 0; i--) {
		ans = ans * 10 + v[i];
	}
	return ans;
}

ll get_divisor(ll n) {
	for (int i = 2; i * i < n; ++i) {
		if (n % i == 0) return i;
	}
	return -1;
}

int main() {
//	freopen("input.txt", "r", stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("Ñ-small.out", "w", stdout);
	ll t, T, i, j, n, ans, p, c = 0;
	string s;
	cin >> T;

	for (t = 0; t < T; ++t) {
		ans = 0;
		cin >> n >> j;
		cout << "Case #" << t + 1 << ":" << endl;
		for (p = 32769; p < 65536; ++p) {
			n = translate2(p);
			if (n % 10 == 0) continue;
			//		n = 1001;
			ll num[11] = { 0 };
			ll div[11] = { 0 };
			bool flag = 0;

			for (i = 2; i < 11; ++i) {
				num[i] = translate10(i, n);
				div[i] = get_divisor(num[i]);
				if (div[i] == -1) {
					flag = 1;
					break;
				}
			}
			if (flag) continue; else c++;

			cout << n;
			for (i = 2; i < 11; ++i) {
				cout << " " << div[i];
			}
			cout << endl;
			if (c == j) break;
		}
	}
	return 0;
}