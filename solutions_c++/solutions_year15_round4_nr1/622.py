//by tzupengwang™
#include<bits/stdc++.h>
using namespace std;

#define FO(it,c) for (__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
typedef long long ll;
typedef pair<int,int> ii;

int r , c ;
char s[ 105 ][ 105 ] ;

void init() {
	cin >> r >> c ;
	for ( int i = 0 ; i < r ; i ++ )
		scanf( "%s" , s[ i ] ) ;
}

char f[ 5 ] = "^v><" ;
int dx[ 5 ] = { -1 , 1 , 0 , 0 } ;
int dy[ 5 ] = { 0 , 0 , 1 , -1 } ;

void process() {
	int ans = 0 ;
	for ( int i = 0 ; i < r ; i ++ ) {
		for ( int j = 0 ; j < c ; j ++ ) {
			int k = 0 ;
			while ( k < 4 && f[ k ] != s[ i ][ j ] ) k ++ ;
			if ( k == 4 ) continue ;
			int ti = i + dx[ k ] , tj = j + dy[ k ] ;
			while ( ti >= 0 && ti < r && tj >= 0 && tj < c && s[ ti ][ tj ] == '.' ) ti += dx[ k ] , tj += dy[ k ] ;
			if ( ti >= 0 && ti < r && tj >= 0 && tj < c ) continue ;
			bool flag = true ;
			for ( k = 0 ; k < 4 ; k ++ ) {
				ti = i + dx[ k ] , tj = j + dy[ k ] ;
				while ( ti >= 0 && ti < r && tj >= 0 && tj < c && s[ ti ][ tj ] == '.' ) {
					ti += dx[ k ] , tj += dy[ k ] ;
				}
				if ( ti >= 0 && ti < r && tj >= 0 && tj < c ) flag = false ;
			}
			if ( flag ) {
				puts( "IMPOSSIBLE" ) ; return ;
			}
			ans ++ ;
		}
	}
	printf( "%d\n" , ans ) ;
}

int main() {
	int Cases;
	scanf( "%d" , &Cases ) ;
	for ( int cases = 1 ; cases <= Cases ; cases ++ ) {
		init() ;
		printf( "Case #%d: " , cases ) ;
		process() ;
	}
	return 0 ;
}

