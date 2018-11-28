#include <bits/stdc++.h>

using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

int main() {
	int t; cin >> t;
	REP(tt, t) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << tt + 1 << ": ";
		REP(i, s) cout << i + 1 << " ";
		cout << endl;
	}
	return 0;
}
