#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define mp make_pair
#define pb push_back

#define MOD 1000000007LL

int main() {
	int t;
	cin >> t;
	int tt;
	for(tt = 1; tt <= t; tt++) {
		string str;
		string m[10];

		m[0] = "ZERO";
		m[1] = "ONE";
		m[2] = "TWO";
		m[3] = "THREE";
		m[4] = "FOUR";
		m[5] = "FIVE";
		m[6] = "SIX";
		m[7] = "SEVEN";
		m[8] = "EIGHT";
		m[9] = "NINE";

		cin >> str;
		int h[26] = {0};
		int h2[10] = {0};
		int i;
		for(i = 0; i < str.size(); i++) {
			h[str[i] - 'A']++;
		}
		vector<pair<int, char> > v;
		v.pb(mp(0, 'Z'));
		v.pb(mp(2, 'W'));
		v.pb(mp(8, 'G'));
		v.pb(mp(4, 'U'));
		v.pb(mp(6, 'X'));
		v.pb(mp(3, 'H'));
		v.pb(mp(1, 'O'));
		v.pb(mp(7, 'S'));
		v.pb(mp(9, 'N'));
		v.pb(mp(5, 'F'));
		for(i = 0; i < v.size(); i++) {
			int val = v[i].first;
			char ch = v[i].second;
			while(h[ch - 'A'] > 0) {
				h2[val]++;
				int j;
				for(j = 0; j < m[val].size(); j++) {
					h[m[val][j] - 'A']--;
				}
			}
		}
		cout << "Case #" << tt << ": ";
		for(i = 0; i < 10; i++) {
			while(h2[i]) {
				cout << i;
				h2[i]--;
			}
		}
		cout << endl;
	}
	return 0;
}