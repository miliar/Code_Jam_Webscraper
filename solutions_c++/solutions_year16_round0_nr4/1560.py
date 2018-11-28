#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
	ll t, k, c, s;
	cin >> t;
	ll numoftest = 1;
	while (t--) {
		cin >> k >> c >> s;
		ll tempnum = pow(k, c - 1);
		cout << "Case #" << numoftest << ": ";
		for (ll i = 0; i < k; i++) {
			cout << 1 + tempnum * i << " ";
		}
		cout << endl;
		numoftest++;
	}
}
