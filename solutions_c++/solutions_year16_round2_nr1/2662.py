#include <bits/stdc++.h>
#include <cmath>
typedef long long ll;
#define get(a) scanf("%lld", &a)
#define repVector(v)  for( auto it = v.begin(); it != v.end(); it++ )
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define FOR(i,a,b) for( ll i = (ll)(a); i <= (ll)(b); i++ )
#define ROF(i,a,b) for( ll i = (ll)(a); i >= (ll)(b); i-- )
#define debug(x) cerr << "[DEBUG] " << #x << " = " << x << endl
#define matrix vector< vector<ll> >
#define F first
#define S second
#define mp make_pair
#define INPFILE freopen("input.in","r",stdin)
#define BOOST ios_base::sync_with_stdio(false); cin.tie(NULL)
using namespace std;

int main() {
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	ll t, c=1; cin >> t;
	while(t--) {
		string s; cin >> s;
		int arr[258] = {0};
		for( char c : s )
			arr[c]++;
		
		vector<int> ans;
		
		pair<string,int> num[] = { { "SIX", 6 },  {"EIGHT", 8 }, { "SEVEN", 7 }, { "THREE", 3 }, { "ZERO", 0 },  { "FIVE", 5 },  { "FOUR", 4 }, { "TWO", 2 }, { "NINE", 9 }, { "ONE", 1 }    };
		ll ptr = 0;
		while( ptr <= 9 ) {
			bool find = 1; string p;
			for( char c : num[ptr].F ) {
			  arr[c]--; p += string(1,c);
			  if( arr[c] < 0 ) {
			  	find = 0;
			  	break;
			  }
			}
			
		//	debug(p);
			
			if( find ) {
			  ans.pb(num[ptr].S);
			}
			else {
			  for( char c : p ) arr[c]++;
			  ptr++;	
			}
		}
		
		sort( all(ans) );
		
		cout << "Case #" << c++ << ": ";
		for( ll x : ans )  cout << x;
		cout << "\n";
	}
}
