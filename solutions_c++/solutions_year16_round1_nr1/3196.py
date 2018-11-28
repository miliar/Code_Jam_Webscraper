#include <bits/stdc++.h>
#define rep(x, to) for (int x = 0; x < (to); x++)
#define REP(x, a, to) for (int x = (a); x < (to); x++)
#define foreach(itr, x) for (typeof((x).begin()) itr = (x).begin(); itr != (x).end(); itr++)
#define EPS (1e-14)
#define _PA(x,N) rep(i,N){cout<<x[i]<<" ";}cout<<endl;
#define _PA2(x,H,W) rep(i,(H)){rep(j,(W)){cout<<x[i][j]<<" ";}cout<<endl;}

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
typedef complex<double> Complex;
typedef vector< vector<int> > Mat;

string ans;

int T;
string s;

string solve() {
	ans = "";
	for (int i = 0; i < s.size(); i++) {
		if (ans + s[i] > s[i] + ans) {
			ans = ans + s[i];
		} else {
			ans = s[i] + ans;
		}
	}
	return ans;
}

int main() {
	cin >> T;
	rep(i, T) {
		cin >> s;
		ans = solve();
		printf("Case #%d: %s\n", i + 1, ans.c_str());
	}
	return 0;
}


