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

int main( void ) {
	freopen( "B-small-attempt0.in", "r", stdin );
	freopen( "B-small-attempt0.out", "w", stdout );
	//srand( time( NULL ) );
	cin >> t;
	forn( _, t ) {
		ll a, b, k;
		cin >> a >> b >> k;
		ll ans = 0;
		forn( i, a ) {
			forn( j, b ) {
				if( ( i & j ) < k )
					ans ++;
			}
		}
		
		cout << "Case #" << _ + 1 << ": ";
		cout << ans << endl;
	}
	
	TIMESTAMP;
	cin >> t;
	return 0;	
}
