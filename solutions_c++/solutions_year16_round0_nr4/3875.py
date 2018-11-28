#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vl = vector<ll>;
using vvl = vector<vl>;
using pll = pair<ll,ll>;
using vb = vector<bool>;
const ll oo = 0x3f3f3f3f3f3f3f3fLL;
const double eps = 1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define has(c,i) ((c).find(i) != end(c))
#define FOR(i,a,b) for (int i=(a); i<(b); i++)       
#define FORD(i,a,b) for (int i=int(b)-1; i>=(a); i--)
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

int main() { 
	ios::sync_with_stdio(false); 
	ll T;
	cin >> T;
	FOR(t,1,T+1){
		ll K, C, S;
		cin >> K >> C >> S;
		cout << "Case #" << t << ":";
		ll step = 1;
		FOR(i,0,C-1) step *= K;
		FOR(i,0,S){
			cout << " " << (step * i)+1;
		}
		cout << endl;
	}
	return 0;
}
