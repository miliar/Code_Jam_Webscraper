#include<stdio.h>
#include<math.h>

int TESTCASE , test ;
__int64 r , t ;
__int64 result ;

int main () {
	freopen ( "A-small-attempt0.in" , "r" , stdin ) ;
	freopen ( "output.txt" , "w" , stdout ) ;

	scanf ( "%d" , & TESTCASE ) ;
	for ( test = 1 ; test <= TESTCASE ; test ++ ) {
		scanf ( "%I64d%I64d" , & r , & t ) ;

		result = (1-2*r+sqrt((2*r-1)*(2*r-1)+8*t))/4 ;

		printf ( "Case #%d: %I64d\n" , test , result ) ;
	}

	return 0 ;
}
