#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1000000 + 100 ;
long long a[ MAXN ] , s[ MAXN ] ;

int main() {
	freopen( "A-small-attempt0.in" , "r" , stdin ) ;
	freopen( "A-small-attempt0.out" , "w" , stdout ) ;
	
	int test_case ;
	cin >> test_case ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		long long n , p , q , r , ss ;
		cin >> n >> p >> q >> r >> ss ;
		s[ 0 ] = 0 ;
		for ( int i = 1 ; i <= n ; i ++ ) {
			a[ i ] = ( ( i - 1 ) * p + q ) % r + ss ;
			s[ i ] = s[ i - 1 ] + a[ i ] ;
		}

		long long ans = -1 ;
		for ( int i = 1 ; i <= n ; i ++ )
			for ( int j = i ; j <= n ; j ++ ) {
				long long a = s[ n ] - s[ i - 1 ] , 
					b = s[ n ] - ( s[ j ] - s[ i - 1 ] ) , 
					c = s[ n ] - ( s[ n ] - s[ j ] ) ;
				ans = max( ans , min( a , min( b , c ) ) ) ;
			}

		printf( "Case #%d: %.10lf\n" , t , ( double ) ans / ( double ) s[ n ] ) ;
		// cout << ans << endl;
	}
}