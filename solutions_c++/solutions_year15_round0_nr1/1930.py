/**
 * Tittle:	Standing Ovation
 * Author:	Cheng-Shih, Wong
 * Date:	2015/04/11
 */

// include files
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

// definitions
#define FOR(i,a,b) for( int i=(a),_n=(b); i<=_n; ++i )
#define clr(x,v) memset( x, v, sizeof(x) )
#define N 1005

// declarations
int t, n;
char buf[N];
int cnt;
int ans;

// functions


// main function
int main( void )
{
	
	// input
	scanf( "%d", &t );

	FOR( ti, 1, t ) {
		scanf( "%d%s", &n, buf );
		
		// solve
		ans = cnt = 0;

		FOR( i, 0, n ) {
			if( cnt<i && buf[i]>'0' ) {
				ans += (i-cnt);
				cnt += (i-cnt);
			}
			
			cnt += buf[i]-'0';
		}

		printf( "Case #%d: %d\n", ti, ans );
	}
	
	return 0;
}
