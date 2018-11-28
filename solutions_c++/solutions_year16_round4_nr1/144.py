#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef pair<ll,ll> pll;
typedef vector<bool> vb;
const ll oo = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c), end(c)
#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define FORD(i,a,b) for (ll i = (b)-1; i >= (a); i--)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define has(c,i) ((c).find(i) != end(c))
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

int main() {
	vector<vector<string>> res(13,vector<string>(3));
	
	res[0] = {"P","R","S"};
	
	FOR(n,1,13) {
		res[n][0] = res[n-1][0] + res[n-1][1];
		res[n][1] = res[n-1][0] + res[n-1][2];
		res[n][2] = res[n-1][1] + res[n-1][2];
	}
	
	ll TC; cin >> TC;
	FOR(tc,1,TC+1) {
		cout << "Case #" << tc << ": ";
		ll n, r, p, s; cin >> n >> r >> p >> s;
		
		bool ok = false;
		for (const string &st : res[n]) {
			map<char,ll> cnt;
			for (const char &c : st) cnt[c]++;
			if (cnt['P'] == p && cnt['R'] == r && cnt['S'] == s) {
				ok = true;
				cout << st << endl;
				break;
			}
		}
		if (!ok) cout << "IMPOSSIBLE" << endl;
	}
}

