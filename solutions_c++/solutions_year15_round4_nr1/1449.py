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

string ch = "^v<>";
ll di[] = {-1,1,0,0}, dj[] = {0,0,-1,1};

ll test() {
	ll m, n; cin >> m >> n;
	vector<string> a(m);
	FOR(i,0,m) cin >> a[i];
	
	FOR(i,0,m) FOR(j,0,n) cerr << a[i][j] << " \n"[j == n-1];

	ll res = 0;
	FOR(i,0,m) FOR(j,0,n) {
		if (a[i][j] == '.') continue;
		bool norot = false;
		bool anyrot = false;
		FOR(dir,0,4) {
			ll ni = i, nj = j;
			bool ok = false;
			while (true) {
				ni += di[dir], nj += dj[dir];
				if (!(ni >= 0 && ni < m && nj >= 0 && nj < n)) break;
				if (a[ni][nj] != '.') {
					ok = true;
					break;
				}
			}
			if (ok) {
				anyrot = true;
				if (ch[dir] == a[i][j]) norot = true;
			}
		}
		if (norot) continue;
		if (!anyrot) return oo;
		res++;
	}
	return res;


}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	ll TC; cin >> TC;
	FOR(tc,1,TC+1) {

		ll res = test();

		cout << "Case #" << tc << ": ";
		if (res < oo) cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;
	}


}

