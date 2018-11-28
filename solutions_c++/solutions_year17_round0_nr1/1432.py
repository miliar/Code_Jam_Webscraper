#include <bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (auto i = t.begin(); i != t.end(); ++i)
#define fi first
#define se second

char opp(char c) {
	return (c == '+') ? '-' : '+';
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	int T;
	string s;
	int k;
	cin >> T;

	int res;
	FOR(t,T) {
		cin >> s >> k;
		res = 0;
		FOR(i, s.length()-k+1) {
			if(s[i] == '-') {
				REP(j, i, i+k-1) {
					s[j] = opp(s[j]);
				}
				res++;
			}
		}
		bool done = true;
		FOR(i, s.length()) {
			if(s[i] == '-') {
				done = false;
				break;
			}
		}
		cout << "Case #" << t+1 << ": ";
		if(done) {
			cout << res;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}
