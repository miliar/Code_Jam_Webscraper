#include <bits/stdc++.h>
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

string foo( string s, ll end ) {
	string p;
	
	ROF(i,end,0)
	 p.pb( ( s[i] == '+' ) ? '-' : '+' );
	FOR(i,end+1,s.size()-1)
	 p.pb( s[i] );
	return p;			
}

int main() {
	//INPFILE;
	freopen("output.out", "w", stdout);
	ll t, c = 0; cin >> t;
	while(t--) {
		string s; cin >> s;
		ll ans = 0;
		
		ROF(i,s.size()-1,0) 
			if( s[i] == '-' ) {
					ll ptr = 0;
					while( s[ptr] == '+' ) ptr++;
					
					 if( ptr > 0 ) {
					  s = foo( s, ptr-1 );
					  ans++;
					 }
					 
					 s = foo( s, i );
					 ans++;
			}
	   
	   printf("Case #%lld: %lld\n", ++c,  ans );
	}
}
