#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>

using namespace std ;

int A[1111] , N , TestCase ;

int main(int argc , char* argv[] ) {
	freopen( "B.in" , "r" , stdin ) ;
	freopen( "B.out" , "w" , stdout ) ;
	scanf( "%d" , &TestCase ) ;
	for( int TC = 1 ; TC <= TestCase ; TC++ ) {
		scanf( "%d" , &N ) ;
		for( int i = 0 ; i < N ; i++ ) {
			scanf( "%d" , &A[i] ) ;
		}
		int l , r , ans = 0 ;
		l = 0 , r = N - 1 ;
		while( l < r ) {
			int MIN = A[l] ;
			int t = l ;
			for( int i = l ; i <= r ; i++ ) {
				if( A[i] < MIN ) {
					MIN = A[i] ;
					t = i ;
				}
			}
			if( t - l < r - t ) {
				for( int i = t ; i > l ; i-- ) {
					A[i] = A[i-1] ;
					ans++ ;
				}
				l++ ;
			} else {
				for( int i = t ; i < r ; i++ ) {
					A[i] = A[i+1] ;
					ans++ ;
				}
				r-- ;
			}
		}
		printf( "Case #%d: %d\n" , TC , ans ) ;
	}
	return 0 ;
}
