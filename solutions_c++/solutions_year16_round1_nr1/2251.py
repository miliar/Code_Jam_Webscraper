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
	INPFILE;
	freopen("output.out", "w", stdout );
	
	int t, c=0; cin >> t;
	while(t--) {
		string s; cin >> s;
		deque<char> str; str.push_back(s[0]);
		
		for( int i = 1; i < s.size(); i++ ) {
			if( s[i] >= str.front() ) str.push_front( s[i] );
			else str.push_back( s[i] ); 
		}
		
		cout << "Case #" << ++c << ": ";
		while( !str.empty() ) {
			cout << str.front();
			str.pop_front();
		}
		cout << '\n';
		
	}
}
