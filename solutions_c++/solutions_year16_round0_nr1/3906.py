#include <bits/stdc++.h>

using namespace std;
#define DEBUG_ON 1

#define INF 0x3f3f3f3f
#define NSYNC ios::sync_with_stdio(false);
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define FOR0(i,b) for(int i=0; i<(b); ++i)
#define TRAV(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define RTRAV(it,c) for(__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define DBG(x) if(DEBUG_ON) cout << #x << " == " << x << endl
#define DBGP(x) if(DEBUG_ON) cout << "(" << (x).first << ", " << (x).second << ")" << endl
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define R(x) scanf(" %d",&(x))
#define RR(x,y) scanf(" %d %d",&(x), &(y))
#define RRR(x,y,z) scanf(" %d %d %d",&(x), &(y),&(z))
#define CLR(v) memset(v, 0, sizeof(v))
#define SET(v) memset(v, -1, sizeof(v))

typedef long long ll;
typedef int int_type;
typedef pair<int_type, int_type> pii;
typedef vector<int_type> vi;
typedef vector<vi> vii;

ll solve(ll base) {
	ll n = base;
	int seen = 0;
	while(true) {
		string s = to_string(n);
		TRAV(it,s) seen |= (1<<(*it-'0'));
		if(seen == ((1<<10)-1)) {
			return n;
		}
		n += base;
	}
}

int main() {
	NSYNC;
	int n;
	cin >> n;
	FOR(t,1,n+1) {
		cout << "Case #" << t << ": ";
		ll val;
		cin >> val;
		if(val==0) cout << "INSOMNIA\n";
		else cout << solve(val) << "\n";
	}
	return 0;
}