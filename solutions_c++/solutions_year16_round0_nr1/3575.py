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

/*
int main2() {
	int t, n;
	cin >> t;
	REP(tt,t) {
		ostringstream oss;
		cin >> n;
		int found = -1;
		REP(i,11) if(i > 0) {
			oss << n * i;
			int good = 1;
			REP(x,10) if(oss.str().find(x+'0') == -1) {
				good = 0;
				break;
			}
			if(good) {
				found = n * i;
				break;
			}
		}
		int good = 1;
		REP(i,10) if(oss.str().find(i+'0') == -1) good = 0;
		cout << "Case #" << tt + 1 << ": ";
		
		if(found == -1) cout << "INSOMNIA" << endl;
		else cout << found << endl;
	}
}
*/

int ans[1000005];

int main() {
	int maxi = -1;
	REP(i,1000001) if(i > 0) {
		int x = 1, mark = (1 << 10) - 1;
		while(x < 75) {
			int now = x * i;
			while(now > 0) mark &= ~(1 << (now % 10)), now /= 10;
			if(mark == 0) {ans[i] = x * i; break;}//{cout << x << endl; maxi = max(maxi, x); break;}//
			x++;
		}
	}
	
	int t, n;
	cin >> t;
	REP(tt,t) {
		cin >> n;
		cout << "Case #" << tt + 1 << ": ";
		if(n == 0) cout << "INSOMNIA" << endl;
		else cout << ans[n] << endl;
	}
}
