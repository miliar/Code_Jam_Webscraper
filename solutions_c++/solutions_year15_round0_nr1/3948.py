#include <bits/stdc++.h>

using namespace std;
#define DEBUG_ON 1

#define INF 0x3f3f3f3f
#define NSYNC ios::sync_with_stdio(false)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define FOR0(i,b) for(int i=0; i<(b); ++i)
#define TRAV(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define RTRAV(it,c) for(__typeof((c).rbegin()) it=(c).rbegin(); it!=(c).rend(); ++it)
#define DBG(x) if(DEBUG_ON) cout << #x << " == " << x << endl
#define DBGP(x) if(DEBUG_ON) cout << "(" << (x).first << ", " << (x).second << ")" << endl
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define CLR(v) memset(v, 0, sizeof(v))
#define SET(v) memset(v, -1, sizeof(v))

typedef long long ll;
typedef int int_type;
typedef pair<int_type, int_type> pii;
typedef vector<int_type> vi;
typedef vector<vi> vii;

int main() {
	NSYNC;
	int tests;
	cin >> tests;
	FOR(t, 1, tests+1) {
		int n;
		cin >> n;
		int ans = 0;
		int p = 0;
		FOR0(i,n+1) {
			char c;
			cin >> c;
			int x = c - '0';
			if(p>=i) {
				p+=x;
			}
			else if(x>0){
				ans += i-p;
				p = i+x;
			}
		}
		cout << "Case #" << t << ": " << ans << "\n";
	}
	return 0;
}