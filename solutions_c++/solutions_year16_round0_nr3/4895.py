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

map<ll,ll> divs;

ll inBase(ll B, string s){
	ll result = 0;
	FOR(i,0,sz(s)){
		result *= B;
		if(s[i] == '1') result += 1;
	}
	return result;
}

ll find_div(ll n){
	if(divs[n] != 0) return divs[n];
	bool found = false;
	FOR(i,2,sqrt(n+1)){
		if((n/i)*i == n){
			divs[n] = i;
			found = true;
			break;
		}
	}
	if(!found)
		divs[n] = -1;
	return divs[n];
}

int main() { 
	ios::sync_with_stdio(false); 
	ll T;
	cin >> T;
	FOR(t,1,T+1){
		ll N, J;
		cin >> N >> J;
		cout << "Case #" << t << ": " << endl;
		FOR(k, 0, 1<<(N-2)){
			string s = "";
			ll todo = k;
			FOR(j,0,N-2){
				if(todo%2) s = "1" + s;
				else s = "0" + s;
				todo /= 2;
			}
			s = "1" + s + "1";
			ll div[9];
			bool poss = true;
			FOR(base, 2, 11){
				div[base-2] = find_div(inBase(base, s));
				if(div[base-2] == -1) poss = false;
			}
			if(poss && J){
				J--;
				cout << s;
				FOR(i,0,9){
					cout << " " << div[i];
				}
				cout << endl;
			}
			if(!J) break;
		}

	}
	return 0;
}
