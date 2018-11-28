#include <algorithm>
#include <cmath>
#include <memory.h>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef long long ll;

ll ret[100];
ll val[100];

ll get(ll val) {
	for (ll i = 2; i * i <= val; ++i)
		if (val % i == 0) return i;
	return -1;
}

bool good(int n, int mask) {
	for (int i = 1; i <= n; ++i) {
		val[n - i + 1] = mask % 2;
		mask /= 2;
	}
	for (int i = 2; i <= 10; ++i) {
		ll cur = 0;
		for (int j = 1; j <= n; ++j) cur = cur * (ll)i + val[j];
		ret[i] = get(cur);
		if (ret[i] == -1) return false;
	}
	return true;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int tst = 1; tst <= test; ++tst) {
		int n, j;
		cin >> n >> j;
		cout << "Case #" << tst << ":" << endl;
		for (ll mask = (1ll << (n - 1)); mask < (1ll << n); ++mask) {
			if (mask % 2 != 1) continue;
			if (j == 0) break;
			if (good(n, mask)) {
		  	vector<ll> val;
		  	val.clear();
		  	ll mask2 = mask;
		  	for (ll k = 0; k < n; ++k) {
		  		val.push_back(mask2 % 2);
		  		mask2 /= 2;	
		  	}
		  	for (ll k = (ll)val.size() - 1; k >= 0; --k) cout << val[k] << ""; cout << " ";
		  	for (ll k = 2; k <= 10; ++k) cout << ret[k] << " "; cout << endl;
		  	--j;
			}
		}
	}
	return 0;           
}