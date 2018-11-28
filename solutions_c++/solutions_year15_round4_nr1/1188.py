#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 100 + 10 ;

const string dc = "<>^v" ;

string g[ MAXN ] ;
int n , m ;

int got( int x , int y ) {
	// cout << "START " << x << ' ' << y << endl;
	char c = g[ x ] [ y ] ;
	int dx = 0 , dy = 0 ;
	if ( c == '^' ) dx = -1 ;
	if ( c == 'v' ) dx = 1 ;
	if ( c == '<' ) dy = -1 ;
	if ( c == '>' ) dy = 1 ;
	x += dx ;
	y += dy ;
	while ( x >= 0 && y >= 0 && x < n && y < m ) {
		if ( g[ x ] [ y ] != '.' )
			return 0 ;
		x += dx ;
		y += dy ;
	} 
	return -1 ;
}

int main() {
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;
	int test_case ;
	cin >> test_case ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		cin >> n >> m ;
		for ( int i = 0 ; i < n ; i ++ ) 
			cin >> g[ i ] ;
		int ans = 0 ;
		for ( int i = 0 ; i < n ; i ++ )
			for ( int j = 0 ; j < m ; j ++ ) {
				if ( ans == -1 ) break ;
				if ( g[ i ] [ j ] == '.' ) continue ;

				char c = g[ i ] [ j ] ;
				// cout << i << ' ' << j << ' ' << got( i , j ) << endl;
				if ( got( i , j ) == -1 ) {
					bool flag = false ;
					for ( int k = 0 ; k < 4 ; k ++ ) {
						g[ i ] [ j ] = dc[ k ] ;
						if ( got( i , j ) == 0 ) {
							flag = true ;
							break ;
						}
					}
					if ( flag )
						ans ++ ;
					else 
						ans = -1 ;
				}
			}
		printf( "Case #%d: " , t ) ;
		if ( ans == -1 )
			printf( "IMPOSSIBLE\n" ) ;
		else
			printf( "%d\n" , ans ) ;
	}
}
