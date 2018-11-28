#include <bits/stdc++.h>
typedef int ll;
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
	INPFILE;
	freopen("output.out","w",stdout);
	int t, c=0; cin >> t;
	while(t--) {
		int n; cin >> n;
		vector< vector<ll> > v( 2*n-1, vector<ll>(n,0) );
		map<int,int> m;
		for( int i = 0; i < 2*n-1; i++ )
		  for( int j = 0; j < n; j++ ) {
		    cin >> v[i][j];
		    m[ v[i][j] ]++;
		  }
		
		cout << "Case #" << ++c << ": ";
		for( auto p : m )
		  if( p.S%2 ) {
		  	cout  << p.F << ' ';
		  }
		cout << '\n';
		
		
	}
}
