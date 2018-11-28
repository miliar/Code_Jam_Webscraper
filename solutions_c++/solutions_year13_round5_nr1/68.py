#include <sstream>
#include <iomanip>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair

#define DEBUG(x) cout << #x << " = "; cout << x << endl;
#define PR(a,n) cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl;
#define PR0(a,n) cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl;
using namespace std;

//Buffer reading
int INP,AM,REACHEOF;
#define BUFSIZE (1<<12)
char BUF[BUFSIZE+1], *inp=BUF;
#define GETCHAR(INP) { \
    if(!*inp) { \
        if (REACHEOF) return 0;\
        memset(BUF,0,sizeof BUF);\
        int inpzzz = fread(BUF,1,BUFSIZE,stdin);\
        if (inpzzz != BUFSIZE) REACHEOF = true;\
        inp=BUF; \
    } \
    INP=*inp++; \
}
#define DIG(a) (((a)>='0')&&((a)<='9'))
#define GN(j) { \
    AM=0;\
    GETCHAR(INP); while(!DIG(INP) && INP!='-') GETCHAR(INP);\
    if (INP=='-') {AM=1;GETCHAR(INP);} \
    j=INP-'0'; GETCHAR(INP); \
    while(DIG(INP)){j=10*j+(INP-'0');GETCHAR(INP);} \
    if (AM) j=-j;\
}
//End of buffer reading

long long b;
vector< pair<long long, long long> > v;
long double best;

void solve() {
	REP(i,v.size()) {
		// cout << v[i].first << ' ' << v[i].second << endl;
	}
	REP(i,v.size()) {
		long long k = v[i].first, c = v[i].second;
		long long cover = 0;
		
		REP(j,i) cover += v[j].second * (k - v[j].first);
		if (cover > b) break;
		
		long long sumc = 0;
		FOR(j,0,i) sumc += v[j].second;
		
		FOR(a,0,sumc) if (a < sumc && b >= cover + a) {
			long long u = (b - cover - a) / sumc;
			
			if (i < v.size() - 1 && k + u >= v[i+1].first) {
				u = v[i+1].first - k - 1;
			}
			
			long long each = k + u;
			
			long double now = 0.0;
			
			int can = sumc - a;			
			REP(j,i+1) {
				long long has = min((int)v[j].second, can);
				now += has * 36 * (each - v[j].first);
				can -= has;
			}
			
			now /= sumc - a;
			now -= cover + a + sumc * u;
			
			// cout << each << ' ' << a << ' ' << now << endl;
			
			best = max(best, now);
		}
	}
}

int main() {
    // freopen("input.txt", "r", stdin);
	int ntest; cin >> ntest;
	cout << (fixed) << setprecision(10);
	FOR(test,1,ntest) {
		int n; cin >> b >> n;
		
		map<long long,int> cnt; cnt.clear();
		FOR(i,1,n) {
			long long u; cin >> u;
			++cnt[u];
		}
		cnt[0] = 37 - n;
		
		v.clear();
		for(map<long long,int> :: iterator it = cnt.begin(); it != cnt.end(); ++it)
			v.PB(MP(it->first, it->second));

		best = 0;
		solve();
		
		cout << "Case #" << test << ": " << best << endl;
	}
    return 0;
}
