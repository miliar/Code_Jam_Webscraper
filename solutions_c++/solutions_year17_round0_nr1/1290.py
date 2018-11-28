#define F(n) Fi(i,n)
#define Fi(i,n) Fl(i,0,n)
#define Fl(i,l,n) for(int i=(l);i<(n);++i)
#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/priority_queue.hpp>
using namespace std;
// using namespace __gnu_pbds;
int k, n, ans;
string s;
bool sol() {
	cin >> s >> k;
	n = s.length(), ans = 0;
	for (int i = 0 ; i + k - 1 < n ; ++i) if (s[i] == '-') {
		Fi(j, k) s[i+j] = (s[i+j] == '+' ? '-' : '+');
		++ans;
	}
	F(n) if (s[i] == '-') return false;
	return true;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	cin >> t;
	Fl(cases, 1, t + 1) {
		cout << "Case #" << cases << ": ";
		if (sol()) cout << ans << '\n';
		else cout << "IMPOSSIBLE\n";
	}
}