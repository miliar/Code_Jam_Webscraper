#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define TIMESTAMP fprintf(stderr, "Execution time: %.3lf s.\n", (double)clock()/CLOCKS_PER_SEC)

#define d				double
#define ll 				long long
#define pb 				push_back
#define mp 				make_pair
#define forn( i, n ) 	for( ll i = 0; i < (ll) (n); i ++ )
#define y1 				dsaddassd
#define endl			'\n'

using namespace std;

ll t;
ll n;

int main( void ) {
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	//srand( time( NULL ) );
	cin >> t;
	forn( _, t ) {
		cin >> n;
		string s[111];
		ll I[111];
		forn( i, n ) {
			cin >> s[i];
			I[i] = 0;
		}
		
		vector< char > c;
		c.pb( s[0][0] );
		forn( i, s[0].size() ) {
			if( s[0][i] == c[c.size() - 1] )
				continue;
			else
				c.pb( s[0][i] );
		}
		
		
		cout << "Case #" << _ + 1 << ": ";

		ll ans = 0;
		ll res[111][111];
		ll m[111], M[111];
		forn( i, n ) {
			forn( j, c.size() ) {
				res[i][j] = 0;	
				m[j] = 100;
				M[j] = 0;
			}	
		}
		bool e = false;
		forn( i, n ) {
			ll k = 0;
			forn( j, s[i].size() ) {
				if( s[i][j] == c[k] ) {
					res[i][k] ++;
				}
				else {
					m[k] = min( m[k], res[i][k] );
					M[k] = max( M[k], res[i][k] );
					k ++;
					if( k >= c.size() ) {
						e = true;
						break;	
					}
					j --;
				}
			}
			if( e )
				break;
			m[k] = min( m[k], res[i][k] );
			M[k] = max( M[k], res[i][k] );
		}
		forn( i, n ) {
			forn( j, c.size() ) {
				if( !res[i][j] ) {
					e = true;	
					break;
				}
			}	
			if( e )
				break;
		}
		if( e ) {
			cout << "Fegla Won" << endl;
			continue;
		}
		forn( i, c.size() ) {
			ll r = 1000000000;
			for( ll j = m[i]; j <= M[i]; j ++ ) {
				ll rr = 0;
				forn( k, n ) {
					rr += abs( j - res[k][i] ); 	
				}
				r = min( rr, r );
			}	
			ans += r;
		}
		

		
		
		cout << ans << endl;
		
	}
	
	TIMESTAMP;
	cin >> t;
	return 0;	
}
