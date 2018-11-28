#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<ll, ll> pll;

const ll oo = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-9;

#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define FORD(i,a,b) for (ll i = ll(b)-1; i >= (a); i--)
#define MAPIT(i,c,k) for (auto i = (c).equal_range((k)).first; i!= (c).equal_range((k)).second; i++)

#define sz(c) ll((c).size())
#define all(c) (c).begin(), (c).end() 
#define mp make_pair
#define pb push_back
#define xx first
#define yy second
#define has(c, i) ((c).find(i) != (c).end())
#define DBG(...) ({ if(1) fprintf(stderr, __VA_ARGS__); })
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

int helper(string& x){
	if(x == ""){
		return 0;
	} else if (x[sz(x)-1] == '+'){
		x = x.substr(0, x.size()-1);
		return helper(x);
	} else {
		string newstring = "";
		if(x[0] == '+'){
			int s = 0;
			while(s < sz(x) && x[s] == '+'){
			s++;
			}

			FORD(i, 0, s){
				newstring += x[i] == '+' ? '-' : '+' ;
			}
			FOR(i, s, sz(x)){
				newstring += x[i] == '+' ? '-' : '+' ;
			}
			return 1 + helper(newstring);
		} else { // '-'
			FORD(i, 0, sz(x)){
				newstring += x[i] == '+' ? '-' : '+' ;
			}
			return 1 + helper(newstring);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(nullptr); 

	ll T; cin >> T;
	FOR(i, 0, T){
		cout << "CASE #" << i+1 << ": ";
		string in;
		cin >> in;
		cout << helper(in) << endl;
	}
	//TODO; 

	return 0;
}
