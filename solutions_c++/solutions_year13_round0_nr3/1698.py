#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

inline bool ispal(ll x) {
	vector<int> dec;
	while (x > 0) {
		dec.push_back(x % 10);
		x /= 10;
	}

	bool res = true;
	for (int i = 0; i < (int) dec.size() / 2; i ++)
		res &= (dec[i] == dec[dec.size() - i - 1]);
	return res;
}

int main() {
	ios::sync_with_stdio(0);

	vector<ll> mem;
	for (ll i = 1; i <= 1e7; i ++)
		if (ispal(i) && ispal(i * i))
			mem.push_back(i * i);

	int T;
	cin >> T;
	for (int t = 0; t < T; t ++) {
		ll A, B;
		cin >> A >> B;
		
		int ans = 0;
		for (int i = 0; i < (int) mem.size(); i ++)
			if (A <= mem[i] && mem[i] <= B)
				ans ++;

		cout << "Case #" << t + 1 << ": " << ans << endl;
	}

	return 0;
}

