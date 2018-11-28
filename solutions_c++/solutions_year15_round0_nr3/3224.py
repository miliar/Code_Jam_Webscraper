/*/**/

#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	map < pair < char, char >, pair < bool, char > > m;
	m[make_pair('i', 'i')] = make_pair(true, '1');
	m[make_pair('i', 'j')] = make_pair(false, 'k');
	m[make_pair('i', 'k')] = make_pair(true, 'j');
	m[make_pair('j', 'i')] = make_pair(true, 'k');
	m[make_pair('j', 'j')] = make_pair(true, '1');
	m[make_pair('j', 'k')] = make_pair(false, 'i');
	m[make_pair('k', 'i')] = make_pair(false, 'j');
	m[make_pair('k', 'j')] = make_pair(true, 'i');
	m[make_pair('k', 'k')] = make_pair(true, '1');
	m[make_pair('1', 'i')] = make_pair(false, 'i');
	m[make_pair('1', 'j')] = make_pair(false, 'j');
	m[make_pair('1', 'k')] = make_pair(false, 'k');
	m[make_pair('i', '1')] = make_pair(false, 'i');
	m[make_pair('j', '1')] = make_pair(false, 'j');
	m[make_pair('k', '1')] = make_pair(false, 'k');
	int t, cnt = 0;
	cin >> t;
	while(t--) {
		int l, x;
		cin >> l >> x;
		string s, foo;
		cin >> foo;
		for(int i = 0; (1 << i) <= x; i++) {
			if(x & (1 << i)) {
				s += foo;
			}
			foo += foo;
		}
		char now = s[0];
		bool sign = false;
		bool have = false;
		for(int i = 1; i < l * x; i++) {
			sign ^= m[make_pair(now, s[i])].first;
			now = m[make_pair(now, s[i])].second;
		}
		if(now != '1' || ! sign) {
			printf("Case #%d: NO\n", ++cnt);
			continue;
		}
		now = s[0];
		sign = false;
		have = false;
		int posi = -1;
		for(int i = 1; i < l * x; i++) {
			if(now == 'i' && ! sign) {
				posi = i - 1;
				have = true;
				break;
			}
			sign ^= m[make_pair(now, s[i])].first;
			now = m[make_pair(now, s[i])].second;
		}
		if(! have) {
			printf("Case #%d: NO\n", ++cnt);
			continue;
		}
		now = s[l * x - 1];
		sign = false;
		have = false;
		int posk = -1;
		for(int i = l * x - 2; i >= 0; i--) {
			if(now == 'k' && ! sign) {
				posk = i + 1;
				have = true;
				break;
			}
			sign ^= m[make_pair(s[i], now)].first;
			now = m[make_pair(s[i], now)].second;
		}
		if(! have) {
			printf("Case #%d: NO\n", ++cnt);
			continue;
		}
		if(posi + 1 < posk) {
			printf("Case #%d: YES\n", ++cnt);
		}
		else {
			printf("Case #%d: NO\n", ++cnt);
		}
	}
	return 0;
}