
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i=0; i<int(n); ++i)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
typedef long long ll;


int TC;
void solve() {
	string s;
	cin >> s;
	int cnt = 0;
	while(!s.empty() && s.back() == '+') {
		s = s.substr(0, sz(s)-1);
	}
	char c = 0;

	rep(i, sz(s)) {
		if (c == s[i]) continue;
		cnt++;
		c = s[i];
	}
	cout << cnt << endl;
}
int main() {
	int T; cin >> T;
	for(int TC=1; TC<=T; TC++) {
		cout << "Case #" << TC << ": ";
		solve();
	}
}

