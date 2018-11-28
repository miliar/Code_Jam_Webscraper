#include<bits/stdc++.h>
using namespace std;
int t, ans, ct, n;
char S[1103];
int main() {
	cin >> t;
	for(int kase = 1; kase <= t; kase++) {
		cin >> n >> S;
		ans = 0;
		ct = S[0] - '0';
		for(int i = 1; i <= n; i++) {
			if(S[i] == '0') {
				continue;
			}
			if(ct < i) {
				ans += (i - ct);
				ct += S[i] - '0' + i - ct;
			} else {
				ct += (S[i] - '0');
			}
		}
		cout << "Case #" << kase << ": " << ans << endl;
	}
}