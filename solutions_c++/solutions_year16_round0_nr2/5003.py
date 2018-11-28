#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, ar[127], n, ans, flip;
	string s;
	cin >> t;
	for(int cs=1; cs<=t; cs++) {
		cin >> s;
		n = (int)s.size();
		for(int i=0; i<n; i++) {
			ar[i] = s[i] == '-' ? 1 : 0;
		}
		ans = 0;
		flip = 1;
		for(int i=n-1; i>=0; i--) {
			if( ar[i] == flip ) {
				ans++;
				flip ^= 1;
			}
		}
		cout << "Case #" << cs << ": " << ans << "\n";
	}
    return 0;
}

