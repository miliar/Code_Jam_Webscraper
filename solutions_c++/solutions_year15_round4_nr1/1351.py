#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<ll, ll> pll;

const ll oo = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define mp make_pair
#define pb push_back
#define xx first
#define yy second
#define DB(X) { if(1) cerr << "DB: " << (#X) << " = " << (X) << endl; }

bool free(ll i, ll j, vector<vector<char>> &f){
	bool isfree = true;
	FOR(d1, -1, 2){
		FOR(d2, -1, 2){
			if(abs(d1) + abs(d2) != 1) continue;
			ll ci = i + d1;
			ll cj = j + d2;
			while(ci >= 0 && cj >= 0 && ci < sz(f) && cj < sz(f[0])){
				if(f[ci][cj] != '.'){
					isfree = false;
					break;
				}
				ci += d1;
				cj += d2;
			}
		}
	}
	return isfree;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll TC;
	cin >> TC;
	FOR(tc, 1, TC+1){
		cout << "Case #" << tc <<": ";
		ll r, c;
		cin >> r >> c;
		vector<vector<char>> f(r, vector<char>(c));
		FOR(i,0,r){
			FOR(j,0,c){
				cin >> f[i][j];
			}
		}
		bool impossible = false;
		ll result = 0;
		FOR(i,0,r){
			ll a = -1;
			FOR(j,0,c){
				if(f[i][j] != '.'){
					a = j;
					break;
				}
			}
			if(a != -1){
				result += (f[i][a] == '<');
				if(free(i, a, f))
					impossible = true;
			}
			a = -1;
			FORD(j,0,c){
				if(f[i][j] != '.'){
					a = j;
					break;
				}
			}
			if(a != -1){
				result += (f[i][a] == '>');
				if(free(i, a, f))
					impossible = true;
			}
		}
		FOR(j,0,c){
			ll a = -1;
			FOR(i,0,r){
				if(f[i][j] != '.'){
					a = i;
					break;
				}
			}
			if(a != -1){
				result += (f[a][j] == '^');
				if(free(a, j, f))
					impossible = true;
			}
			a = -1;
			FORD(i,0,r){
				if(f[i][j] != '.'){
					a = i;
					break;
				}
			}
			if(a != -1){
				result += (f[a][j] == 'v');
				if(free(a, j, f))
					impossible = true;
			}
		}
		if(impossible)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << result << endl;
	}
}
