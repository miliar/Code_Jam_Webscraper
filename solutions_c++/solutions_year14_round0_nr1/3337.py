#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	freopen( "A-small-attempt0.in" , "r" , stdin ) ;
	freopen( "A-small.out" , "w" , stdout ) ;

	int test_case ;
	scanf( "%d" , &test_case ) ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		int a[ 4 ] , b[ 4 ] , c[ 4 ] ;
		int row ;

		scanf( "%d" , &row ) ;
		for ( int i = 1 ; i <= 4 ; i ++ )
			for ( int j = 0 ; j < 4 ; j ++ )
			{
				int c ;
				scanf( "%d" , &c ) ;
				if ( i == row ) 
					a[ j ] = c ;
			}


		scanf( "%d" , &row ) ;
		for ( int i = 1 ; i <= 4 ; i ++ )
			for ( int j = 0 ; j < 4 ; j ++ )
			{
				int c ;
				scanf( "%d" , &c ) ;
				if ( i == row ) 
					b[ j ] = c ;
			}

		memset( c , 0 , sizeof( c ) ) ;
		for ( int i = 0 ; i < 4 ; i ++ )
			for ( int j = 0 ; j < 4 ; j ++ )
				if ( a[ i ] == b[ j ] )
					c[ i ] = 1 ;

		int count = 0 , ans ;
		for ( int i = 0 ; i < 4 ; i ++ )
			if ( c[ i ] ) {
				ans = a[ i ] ;
				count ++ ;
			}

		printf( "Case #%d: " , t ) ;
		if ( count == 0 )
			printf( "Volunteer cheated!\n" ) ;
		if ( count == 1 )
			printf( "%d\n" , ans ) ;
		if ( count > 1 ) 
			printf( "Bad magician!\n" ) ;
	}
}
