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

map<vi, int> mp;

int solve(const vi& v) {
	if(v.empty()) return 0;
	auto it = mp.find(v);
	if(it != mp.end()) return it->second;
	int ans = INF;
	vi do_nothing;
	TRAV(it, v)
		if(*it > 1) do_nothing.pb(*it-1);
	ans = min(ans, solve(do_nothing) + 1);
	int max_elt = v.back();
	FOR(rem, 1, max_elt){
		vi split_max(v);
		split_max.back() = rem;
		split_max.pb(max_elt - rem);
		sort(split_max.begin(), split_max.end());
		ans = min(ans, solve(split_max)+1);
	}
	return mp[v] = ans;
}

int main() {
	NSYNC;
	int tests;
	cin >> tests;
	FOR(t, 1, tests+1) {
		vi v;
		int d;
		cin >> d;
		while(d--) {
			int x;
			cin >> x;
			v.pb(x);
		}
		mp.clear();
		sort(v.begin(), v.end());
		cout << "Case #" << t << ": " << solve(v) << "\n";
	}
	return 0;
}