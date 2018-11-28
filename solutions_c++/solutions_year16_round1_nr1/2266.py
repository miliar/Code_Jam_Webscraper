#include <bits/stdc++.h>
using namespace std;

int T;
string S;

int main() {
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> S;
		string ans(S.substr(0,1));
		for (int i=1; i<S.length(); i++)
			if (S[i] >= ans[0]) ans = S[i] + ans;
			else ans += S[i];
		cout << "Case #" << t << ": " << ans << endl;
	}
}
