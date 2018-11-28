#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define ll long long



vector<int> getBits(int x) {
	vector<int> v;
	while (x) {
		v.pb(x % 2);
		x /= 2;
	}
	reverse(v.begin(), v.end());
	return v;
}

ll getNumber(ll base, vector<int> &v) {
	ll currCuCat = 1LL;
	ll number = 0;
	for (int i = 0; i < v.size(); ++i) {
		number = number + 1LL * v[i] * currCuCat;
		currCuCat *= base;
	}
	return number;
}

int main() {
	ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	//freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	#endif

	cout << "Case #1:\n";
	int cate = 0;


	for (int i = 3; i < 2 ^ 20; ++i) {
		vector<int> bits = getBits(i);
		if (bits.size() != 16) {
			continue;
		}
		if (bits[0] != 1 || bits[bits.size() - 1] != 1) {
			continue;
		}
		vector<int> ans;
		for (int base = 2; base <= 10; ++base) {
			ll number = getNumber(base, bits);

			for (ll j = 2LL; 1LL * j * j <= number; j++) {
				if ((number % j) == 0) {
					//cout << number << " " << base << " " << j << "\n";
					ans.pb(j);
					break;
				}
			}
		}

		if (ans.size() == 9) {
			++cate;
			if (cate == 51) {
				break;
			}
			//cout << getNumber(2, bits) << "\n";
			for (int j = bits.size() - 1; j >= 0; --j) {
				cout << bits[j];
			}
			cout << " " ;

			for (int j = 0; j < ans.size(); ++j) {
				cout << ans[j] << " ";
			}
			cout << "\n";
		}

	}

	return 0;
}