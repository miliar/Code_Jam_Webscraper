#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define endl '\n'

int main() {
	ios::sync_with_stdio(0);
	int t; cin >> t;
	for (int T=1; T<=t; T++) {
		string s; cin >> s;
		cout << "Case #" << T << ": ";
		int ans = 0;
		int i=s.length()-1;
		while(s[i] == '+') i--;
		s = s.substr(0,i+1);
		char prev = s[s.length()-1];
		if (prev == '-') ans++;
		for (int i=s.length()-1; i>=0; i--) {
			if (s[i] != prev) ans++;
			prev = s[i];
		}
		cout << ans;
		if (T != t) cout << endl;
	}
	return 0;
}