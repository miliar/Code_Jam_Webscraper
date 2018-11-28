#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	freopen( "D-large.in" , "r" , stdin ) ;
	freopen( "D-large.out" , "w" , stdout ) ;

	int test_case ;
	scanf( "%d" , &test_case ) ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		int n ;
		double a[ 1000 ] , b[ 1000 ] ;
		scanf( "%d" , &n ) ;
		for ( int i = 0 ; i < n ; i ++ ) scanf( "%lf" , a + i ) ;
		for ( int i = 0 ; i < n ; i ++ ) scanf( "%lf" , b + i ) ;
		sort( a , a + n ) ;
		sort( b , b + n ) ;

		int al = 0 , ar = n - 1 ;
		int bl = 0 , br = n - 1 ;
		int ans1 = 0 ;
		for ( int i = 0 ; i < n ; i ++ ) {
			if ( a[ al ] > b[ bl ] ) {
				ans1 ++ ; 
				al ++ ;
				bl ++ ;
			} else {
				if ( a[ al ] > b[ br ] )
					ans1 ++ ;
				al ++ ;
				br -- ;
			}
		}

		al = 0 ; ar = n - 1 ;
		bl = 0 ; br = n - 1 ;
		int ans2 = 0 ;
		for ( int i = 0 ; i < n ; i ++ ) {
			if ( b[ br ] < a[ ar ] ) {
				ans2 ++ ;
				bl ++ ;
				ar -- ;
			} else {
				br -- ;
				ar -- ;
			}
		}

		printf( "Case #%d: %d %d\n" , t , ans1 , ans2 ) ;
	}
}
