#include<stdio.h>
#include<math.h>

int a , b ;
int output ;
int num [ 100 ] , str ;

int main () {
	freopen ( "input.txt" , "r" , stdin ) ;
	freopen ( "output.txt" , "w" , stdout ) ;
	int TESTCASE , test ;
	int i , j , k , l ;
	scanf ( "%d" , &TESTCASE ) ;
	for ( test = 1 ; test <= TESTCASE ; test ++ ) {
		
		scanf ( "%d%d" , & a , & b ) ;
		//printf ( "%d %d\n" , a , b ) ;

		output = 0 ;

		for ( k = 1 ; k <= 100 ; k ++ ) {
			l = k*k ;
			if ( l < a ) continue ;
			if ( l > b ) break ;

			i = k ;
			//printf ( "%d\n" , i ) ;
			for ( str = 0 ; i ; str ++ ) {
				num [ str ] = i %10 ;
				i /= 10 ;
			}
			for ( i = 0 ; i < str ; i ++ ) if ( num [ i ] != num [ str - 1 - i ] ) break ;
			if ( i != str ) continue ;

			i = l ;
			for ( str = 0 ; i ; str ++ ) {
				num [ str ] = i %10 ;
				i /= 10 ;
			}
			for ( i = 0 ; i < str ; i ++ ) if ( num [ i ] != num [ str - 1 - i ] ) break ;
			if ( i != str ) continue ;
			output ++ ;

		}
		//printf ( "\n" ) ;

		printf ( "Case #%d: %d\n" , test , output ) ;

	}
	return 0 ;
}