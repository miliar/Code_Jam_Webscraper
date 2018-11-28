#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=(a);i<(b);++i)
typedef long long lint;

int solve() {
	string s;
	cin >> s;
	
	int res = 0;
	
	char c = s[0];
	
	int n = s.size();
	
	for_(i,1,n) {
		if (c != s[i]) {
			c = s[i];
			++res;
		}
	}
	
	return res + (s[n - 1] == '-');
}

int main() {
	int T;
	cin >> T;
	
	for_(i,0,T) {
		int ans = solve();
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}