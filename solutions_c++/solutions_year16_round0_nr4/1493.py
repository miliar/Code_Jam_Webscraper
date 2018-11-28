#include <iostream>
#include <string>
#include <cmath>

#define ll long long

using namespace std;



void solve() {
	ll k,c,s;
	cin >> k >> c >> s;

	if (c==1) {
		if (k > s) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}

		for(int i = 0; i < k; i++) {
			cout << i + 1 << " ";
		}
		cout << endl;
		return;
	}

	ll num = (k + 1) / 2;

	if (s < num) {
		cout << "IMPOSSIBLE" << endl;
		return ;
	}
	ll k_len = 1;
	for (ll i = 0; i < c-1; i++) {
		k_len*=k;
	}
	ll k_max = max(1LL,k_len * k - 1);

	
	ll pos = 0;
	for (ll i = 0; i < num; i++) {
		pos = min((k_len * 2) * i + i * 2 + 2,k_max);
		cout << pos << " "; 
	}
	//cout << " k_len:" << k_len << " k:" << k << " c:" << c << endl;
	cout << endl;
}


int main() {
	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}