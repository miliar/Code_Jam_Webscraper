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
#define ST 1000000000

using namespace std;

ll t;

int main( void ) {
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	//srand( time( NULL ) );
	cin >> t;
	forn( _, t ) {
		double c, f, x;
		cin >> c >> f >> x;
		double ans = 0.0;
		double res = 2.0;
		while( x / ( res + f ) + c / res < x / res ) {
			ans += c / res;
			res += f;
		}
		ans += x / res;
		cout << "Case #" << _ + 1 << ": "; 
		printf( "%.7f \n", ans );
			

	}
	
	TIMESTAMP;
	cin >> t;
	return 0;	
}
