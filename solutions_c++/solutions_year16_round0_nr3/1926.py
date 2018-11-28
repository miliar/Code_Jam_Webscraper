#include <iostream>
using namespace std;

typedef long long ll;

int getDivisor(ll x) {
	if (x % 2 == 0) return 2;
	for (ll i = 3; i*i <= x+10; i+=2)
		if (x % i == 0) return i;
	return -1;
}

long long convertInBase(ll x, int base) {
	ll res = 0;
	ll e = 1;
	while (x) {
		res += e * (x % 2);
		e *= base;
		x /= 2;
	}
	return res;
}

int main() {
	int T; cin >> T;
	int N, J;
	cin >> N >> J;
	cout << "Case #1:" << endl;
	for (ll i = (((ll)1)<<(N-1))+1; J && i <= (((ll)1)<<N)-1; i += 2) {
		ll div[10];
		bool ok = true;
		for (int b = 2; b <= 10 && ok; b++) {
			ll k = convertInBase(i, b);
			ll d = getDivisor(k);
			if (d == -1) {
				ok = false;
			}
			div[b] = d;
		}
		if (ok) {
			J--;
			cout << convertInBase(i, 10) << " ";
			for (int b = 2; b <= 10; b++)
				cout << (long long)div[b] << " ";
			cout << endl;
		}
	}
}
