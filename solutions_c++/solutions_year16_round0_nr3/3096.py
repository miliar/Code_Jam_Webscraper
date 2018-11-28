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
#define LIM 1000

int comp[LIM + 5] = {};

int main() {
	vector <int> prime;
	comp[0] = comp[1] = 1;
	for(int i = 2; i * i <= LIM; i++)
		for(int j = 2 * i; j <= LIM; j += i)
			comp[j] = 1;
	REP(i,LIM) if(!comp[i]) prime.pb(i);
	
	int tt, nn, jj; cin >> tt >> nn >> jj;
	cout << "Case #1:\n";
	for(int i = (1 << 15) + 1; i < (1 << 16); i++) if(i % 2 != 0) {
		int ok = 1, divi[11] = {};
		long long tenbase = 0;
		REP(base, 11) if(base > 1) {
			long long cur = 1, tot = 0, now = i;
			while(now > 0) {
				if(now % 2) tot += cur;
				cur *= base;
				now >>= 1;
			}
			if(base == 10) tenbase = tot;
			int found = 0;
			REP(j, sz(prime)) if(tot % prime[j] == 0) {
				found = 1;
				divi[base] = prime[j];
				break;
			}
			if(found == 0) {
				ok = 0;
				break;
			}
		}
		//if(ok) ans.pb(i);
		if(ok) {
			cout << tenbase << " ";
			REP(base, 11) if(base > 1) cout << divi[base] << " ";
			cout << endl;
			jj--;
		}
		if(jj == 0) break;
	}
}
