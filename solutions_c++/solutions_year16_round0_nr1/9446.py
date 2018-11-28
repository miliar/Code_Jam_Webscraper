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
		ll a; cin >> a;
		cout << "Case #" << T << ": ";
		if (a == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		set<int> seen;
		string s = to_string(a);
		for (int i=0; i<s.length(); i++) {
			seen.insert(s[i]-'0');
		}
		ll b = a;
		while(seen.size() < 10) {
			b += a;
			s = to_string(b);
			for (int i=0; i<s.length(); i++) {
				seen.insert(s[i]-'0');
			}
			if (seen.size() == 10) {
				break;
			}
		}
		cout << b << endl;
	}
	return 0;
}