/**
 * Tittle:	Infinite House of Pancakes
 * Author:	Cheng-Shih, Wong
 * Date:	2015/04/11
 */

// include files
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

// definitions
#define FOR(i,a,b) for( int i=(a),_n=(b); i<=_n; ++i )
#define clr(x,v) memset( x, v, sizeof(x) )
#define pb push_back
#define N 1005

typedef vector<int> VI;

// declarations
int t;
int d;
int p[N];
VI pl;
int ans;

// functions


// main function
int main( void )
{
	int tmp, maxt;
	int v;
	
	// input
	scanf( "%d", &t );

	FOR( ti, 1, t ) {
		scanf( "%d", &d );
		pl.clear();
		clr( p, 0 );

		maxt = 0;
		FOR( i, 1, d ) {
			scanf( "%d", &tmp );
			if( !p[tmp] ) {
				maxt = max( maxt, tmp );
				pl.pb(tmp);
			}
			++p[tmp];
		}

		// solve
		ans = maxt;
		FOR( i, 1, maxt ) {
			tmp = i;
			for( VI::iterator it=pl.begin(); it!=pl.end(); ++it ) {
				tmp += p[(*it)]*(((*it)+i-1)/i-1);
			}
			ans = min( ans, tmp );
		}

		// output
		printf( "Case #%d: %d\n", ti, ans );
	}
	
	return 0;
}
