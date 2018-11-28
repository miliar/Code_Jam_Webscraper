#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt) {
		string str; 
		int n, k;
		
		cin >> str >> k;
		n = str.size();

		int ans = 0;
		for(int i = 0; i + k <= n; ++i) {
			if(str[i] == '-') {
				++ans;
				for(int j = 0; j < k; ++j)
					str[i + j] ^= ('-' ^ '+');
			}
		}

		bool bad = false;
		for(auto &c : str)
			bad |= (c == '-');

		cout << "Case #" << tt << ": ";
		if(bad) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}
	return 0;
}