#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for(int i = 0;i < n;++i)
#define FOR(i, a, b) for(int i = a;i < b;++i)

string s;
int n;

bool check() {
	bool yes = true;
	REP(i, n + 1) if(s[i] != '0') {
		yes = false;
		break;
	}
	return yes;
}

int solve() {
	if(check()) return 0;
	int x, cnt = 0, r = 0;
	if(s[0] == '0') {
		++r;
		cnt = 1;
	}
	else cnt = s[0] - '0';

	FOR(i, 1, n + 1) {
		x = s[i] - '0';
		if(!x) continue;
		if(cnt >= i) cnt += x;
		else {
			r += i - cnt;
			cnt = i + x;
		}
	}
	return r;
}

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	REP(i, t) {
		cin >> n >> s;
		if(!n) cout << "Case #" << i + 1 << ": " << 0 << "\n";
		else cout << "Case #" << i + 1 << ": " << solve() << "\n";
	}
}