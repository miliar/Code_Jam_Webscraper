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

ll m, n, N;

ll di[] = {-1,0,1,0}, dj[] = {0,1,0,-1};

struct pos { ll i, j, dir; };

pos border(ll i) {
	if (i < n) return {-1,i,2};
	i -= n;
	if (i < m) return {i,n,3};
	i -= m;
	if (i < n) return {m,n-i-1,0};
	i -= n;
	return {m-i-1,-1,1};
}

bool ok(vector<string> &a, vl &b) {
	FOR(i,0,m+n) {
		pos p = border(b[2*i]); 		
		p.i += di[p.dir], p.j += dj[p.dir];
		while (p.i >= 0 && p.i < m && p.j >= 0 && p.j < n) {
			if (a[p.i][p.j] == '/') p.dir = p.dir ^ 1;
			else p.dir = 3 - p.dir;
			p.i += di[p.dir], p.j += dj[p.dir];
		}
		pos q = border(b[2*i+1]);
		if (p.i != q.i || p.j != q.j) return false;
	}
	return true;
}

int main() {
	ll TC; cin >> TC;
	FOR(tc,1,TC+1) {
		cout << "Case #" << tc << ":" << endl;
		
		cin >> m >> n;
		N = m*n;
		vl b(2*(m+n));
		FOR(i,0,2*(m+n)) cin >> b[i], b[i]--;
		bool done = false;
		FOR(mask,0,1 << N) {
			vector<string> a(m,string(n,' '));
			FOR(I,0,N) {
				ll i = I / n, j = I % n;
				a[i][j] = (mask & (1 << I)) ? '/' : '\\';
			}
			if (ok(a,b)) {
				FOR(i,0,m) cout << a[i] << endl;
				done = true;
				break;
			}
		}	
		if (!done) cout << "IMPOSSIBLE" << endl;
	}


}

