#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

#define N 1005

int t, ti = 0;
double naomi[N], ken[N];
int n;

const int game( const double *a, const double *b )
{
	int win = 0;
	static int al, bl, ar, br;

	al = bl = 1;
	ar = br = n;

	while( al <= ar ) {
		if( a[al] > b[bl] ) {
			++win;
			++al; ++bl;
		} else {
			++al; --br;
		}
	}

	return win;
}

int main( void )
{
	int i;

	scanf( "%d", &t );

	while( t-- ) {
		scanf( "%d", &n );

		for( i = 1; i <= n; ++i ) scanf( "%lf", &naomi[i] );
		for( i = 1; i <= n; ++i ) scanf( "%lf", &ken[i] );

		sort( naomi+1, naomi+1+n );
		sort( ken+1, ken+1+n );

		printf( "Case #%d: %d %d\n", ++ti, game(naomi,ken), n-game(ken,naomi) );
	}


	return 0;
}
