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

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(nullptr); 

	ll T; cin >> T;
	FOR(i, 0, T){
		cout << "CASE #" << i+1 << ": ";
		vector<bool> m (10);
		ll erg = 0;

		ll num;
		cin >> num;
		if(!num){
			cout << "INSOMNIA"<<endl;
		} else{
			ll count = 0;
			ll mul = 0;

			while(erg != 10){
				count++;
				mul = count * num;
				string a = to_string(mul);
				for(auto c : a){
					if(!m[c-'0']){
						erg++;
						m[c-'0']=true;
					}
				}
			}
			cout << mul << endl;
		}
	}
	//TODO; 

	return 0;
}
