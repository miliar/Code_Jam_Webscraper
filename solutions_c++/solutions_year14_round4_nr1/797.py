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

int A[11111] ;
int TestCase , N , S ;

int main(int argc , char* argv[] ) {
	freopen( "A.in" , "r" , stdin ) ;
	freopen( "A.out" , "w" , stdout ) ;
	scanf( "%d" , &TestCase ) ;
	for( int TC = 1 ; TC <= TestCase ; TC++ ) {
		scanf( "%d%d" , &N , &S ) ;
		for( int i = 0 ; i < N ; i++ ) {
			scanf( "%d" , &A[i] ) ;
		}
		sort( A , A + N ) ;
		int i = 0, j = N - 1 ;
		int ans = N ;
		while( i < j ) {
			if( A[i] + A[j] <= S ) {
				ans-- ;
				i++, j-- ;
			} else {
				j-- ;
			}
		}
		printf( "Case #%d: %d\n" , TC , ans ) ;
	}
	return 0 ;
}
