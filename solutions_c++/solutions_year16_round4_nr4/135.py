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

bool dfs(ll i, ll n, vector<string> &a, vl &p, ll mask = 0) {
	if (i == n) return true;
	bool can = false;
	FOR(j,0,n) if (!(mask & (1 << j)) && a[p[i]][j] == '1') {
		can = true;
		if (!dfs(i+1,n,a,p,mask ^ (1 << j))) return false;
	}
	return can;
}

bool ok(ll n, vector<string> &a) {
	vl p(n);
	FOR(i,0,n) p[i] = i;
	do {
		if (!dfs(0,n,a,p)) return false;
	} while (next_permutation(all(p)));
	return true;
}

int main() {
	ll TC; cin >> TC;
	FOR(tc,1,TC+1) {
		cout << "Case #" << tc << ": ";
		
		ll n; cin >> n;
		vector<string> b(n);
		FOR(i,0,n) cin >> b[i];
		ll N = n*n;
		ll res = oo;
		FOR(mask,0,1 << N) if (__builtin_popcount(mask) < res) {
			vector<string> a = b;
			FOR(I,0,N) if (mask & (1 << I)) {
				ll i = I / n, j = I % n;
				a[i][j] = '1';
			}
			if (ok(n,a)) res = __builtin_popcount(mask);
		}
		cout << res << endl;	
	}


}

