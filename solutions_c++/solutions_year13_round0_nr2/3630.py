#include<stdio.h>

int n , m ;
int height [ 102 ][ 102 ] ;
int height_x [ 102 ] , height_y [ 102 ] ;

int main () {
	freopen ( "input.txt" , "r" , stdin ) ;
	freopen ( "output.txt" , "w" , stdout ) ;
	int i , j ;
	int TESTCASE , test ;
	scanf ( "%d" , &TESTCASE ) ;
	for ( test = 1 ; test <= TESTCASE ; test ++ ) {
		printf ( "Case #%d: " , test ) ;

		scanf ( "%d%d" , & n , & m ) ;

		for ( i = 1 ; i <= n ; i ++ ) height_x [ i ] = 0 ;
		for ( i = 1 ; i <= m ; i ++ ) height_y [ i ] = 0 ;

		for ( i = 1 ; i <= n ; i ++ ) {
			for ( j = 1 ; j <= m ; j ++ ) {
				scanf ( "%d" , & height [ i ][ j ] ) ;
				if ( height [ i ][ j ] > height_x [ i ] ) height_x [ i ] = height [ i ][ j ] ;
				if ( height [ i ][ j ] > height_y [ j ] ) height_y [ j ] = height [ i ][ j ] ;
			}
		}
		for ( i = 1 ; i <= n ; i ++ ) {
			for ( j = 1 ; j <= m ; j ++ ) {
				if ( height [ i ][ j ] < height_x [ i ] && height [ i ][ j ] < height_y [ j ] ) {
					printf ( "NO\n" ) ;
					break ;
				}
			}
			if ( j <= m ) break ;
		}
		if ( i == n + 1 ) printf ( "YES\n" ) ;
	}
	return 0 ;
}