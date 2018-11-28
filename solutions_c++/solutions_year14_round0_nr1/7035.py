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

#define ll long long
#define pb push_back
#define mp make_pair
#define forn( i, n ) for( ll i = 0; i < (ll) (n); i ++ )
#define y1 dsaddassd

using namespace std;

ll t;

int main( void ) {
	freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "A-small-attempt0.out", "w", stdout );
	//srand( time( NULL ) );
	cin >> t;
	forn( _, t ) {
		bool b[17][2];
		forn( i, 17 ) {
			b[i][0] = b[i][1] = false;	
		}
		forn( i, 2 ) {
			ll a;
			cin >> a;
			forn( j, 4 )
				forn( k, 4 ) {
					ll c;
					cin >> c;
					if( a == j + 1 )
						b[c][i] = true;
				}
		}
		ll res = 0;
		ll ans = 0;
		forn( i, 17 ) {
			if( b[i][0] == true && b[i][1] == true ) {
				res ++;
				ans = i;	
			}	
		}
		cout << "Case #" << _ + 1 << ": "; 
		if( res == 0 ) 
			cout << "Volunteer cheated!" << endl;
		else if( res == 1 ) 
			cout << ans << endl;
		else 
			cout << "Bad magician!" << endl;
			

	}
	
	TIMESTAMP;
	cin >> t;
	return 0;	
}
