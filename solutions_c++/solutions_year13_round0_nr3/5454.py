#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
	
	int t, a, b, i, count, ct = 1;

	int A[ 5 ] = { 1, 4, 9, 121, 484 };

	scanf("%d" ,&t );
	
	while( ct <= t ) {

		scanf("%d %d", &a, &b );

		count = 0;
		for( i = 0;i < 5;i++ )
			if( ( A[ i ] >= a ) && ( A[ i ] <= b ) )
				count++;
		
		printf("Case #%d: %d\n", ct, count ); 	
		ct++;
	}
	
	return 0;

}

