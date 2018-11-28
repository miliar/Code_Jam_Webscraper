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

int main() {
	freopen("output.out","w",stdout);
	
	ll t, c=0; cin >> t;
	while(t--) {
		ll n; cin >> n;
		printf("Case #%lld: ", ++c);
		
		if( n == 0 ) {
			cout << "INSOMNIA\n";
			continue;
		}
		
		ll bit = 0, no = n;
		while( bit+1 != (1LL<<10) ) {
			ll num = no;
			while( num > 0 ) {
				bit |= ( 1LL<<(num%10) );
				num /= 10;
			}
			no += n;			
		}
		
		cout << no - n << '\n';
		
	}
}
