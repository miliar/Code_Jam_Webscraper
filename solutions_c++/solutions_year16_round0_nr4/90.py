#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	int _;
	cin >> _;
	for(int __ = 0; __ < _;) {
		cout << "Case #" << ++__ << ": ";	
		ll k, c, s;
		cin >> k >> c >> s;
		if(s < (k+c-1)/c) cout << "IMPOSSIBLE\n";
		else {
			for(int i = 0; i < k; i += c) {
				long long u = 0;
				for(int j = 1; j <= c; j++) {
					u *= k;
					long long a = j+i;
					if(a > k) a = k;
					u += a-1;
				}
				cout << u+1 << " ";
			}
			cout << "\n";
		}
	}
	return 0;
}
