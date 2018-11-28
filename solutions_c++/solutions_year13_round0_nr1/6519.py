#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

bool checkX( char c1, char c2, char c3, char c4 ) {

	return ( ( c1 == 'X' ) && ( c2 == 'X' ) && ( c3 == 'X' ) && ( c4 == 'X' ) );
}

bool checkO( char c1, char c2, char c3, char c4 ) {

	return ( ( c1 == 'O' ) && ( c2 == 'O' ) && ( c3 == 'O' ) && ( c4 == 'O' ) );
}

bool checkXT( char c1, char c2, char c3, char c4 ) {

	return ( ( ( c1 == 'X' ) && ( c2 == 'X' ) && ( c3 == 'X' ) && ( c4 == 'T' ) ) || ( ( c1 == 'X' ) && ( c2 == 'X' ) && ( c3 == 'T' ) && ( c4 == 'X' ) ) || ( ( c1 == 'X' ) && ( c2 == 'T' ) && ( c3 == 'X' ) && ( c4 == 'X' ) ) || ( ( c1 == 'T' ) && ( c2 == 'X' ) && ( c3 == 'X' ) && ( c4 == 'X' ) ) );
}

bool checkOT( char c1, char c2, char c3, char c4 ) {

	return ( ( ( c1 == 'O' ) && ( c2 == 'O' ) && ( c3 == 'O' ) && ( c4 == 'T' ) ) || ( ( c1 == 'O' ) && ( c2 == 'O' ) && ( c3 == 'T' ) && ( c4 == 'O' ) ) || ( ( c1 == 'O' ) && ( c2 == 'T' ) && ( c3 == 'O' ) && ( c4 == 'O' ) ) || ( ( c1 == 'T' ) && ( c2 == 'O' ) && ( c3 == 'O' ) && ( c4 == 'O' ) ) );

}

void printMatrix( char A[ 4 ][ 4 ] ) {

	int i, j;

		for( i = 0;i < 4;i++ ) {
			for( j = 0;j < 4;j++ ) 				
				printf("%c", A[ i ][ j ] );
			printf("\n");	
		}
}

int main() {
	
	int t, i, j, flagVal, ct = 1, newFlag;
	
	scanf("%d", &t );
	
	while( ct <= t ) {
		
		scanf("\n");
		char A[ 4 ][ 4 ];
		
		flagVal = 1;

		for( i = 0;i < 4;i++ ) {
			for( j = 0;j < 4;j++ ) {
				
				scanf("%c", &A[ i ][ j ] );
				if( A[ i ][ j ] == '.' )
					flagVal = 0;		
			}
				scanf("\n");	
		}

//		printMatrix(A);
	
		newFlag = 1;

		for( i = 0;i < 4;i++ ) {
				
			if( checkX( A[ i ][ 0 ], A[ i ][ 1 ], A[ i ][ 2 ], A[ i ][ 3 ] ) )	{	
				printf("Case #%d: X won\n", ct );
				newFlag = 0;
				break;
			}
			
			else if( checkO( A[ i ][ 0 ], A[ i ][ 1 ], A[ i ][ 2 ], A[ i ][ 3 ] ) ) {
				printf("Case #%d: O won\n", ct );
				newFlag = 0;
				break;
			}

			else if( checkXT( A[ i ][ 0 ], A[ i ][ 1 ], A[ i ][ 2 ], A[ i ][ 3 ] ) ) {
				printf("Case #%d: X won\n", ct );		
				newFlag = 0;
				break;
			}

			else if( checkOT( A[ i ][ 0 ], A[ i ][ 1 ], A[ i ][ 2 ], A[ i ][ 3 ] ) ) {
				printf("Case #%d: O won\n", ct );	
				newFlag = 0;
				break;
			}

			else if( checkX( A[ 0 ][ i ], A[ 1 ][ i ], A[ 2 ][ i ], A[ 3 ][ i ] ) ) {
				printf("Case #%d: X won\n", ct );
				newFlag = 0;
				break;
			}

			else if( checkO( A[ 0 ][ i ], A[ 1 ][ i ], A[ 2 ][ i ], A[ 3 ][ i ] ) ) {					
				printf("Case #%d: O won\n", ct );
				newFlag = 0;
				break;
			}

			else if( checkXT( A[ 0 ][ i ], A[ 1 ][ i ], A[ 2 ][ i ], A[ 3 ][ i ] ) ) {					
				printf("Case #%d: X won\n", ct );
				newFlag = 0;
				break;
			}

			else if( checkOT( A[ 0 ][ i ], A[ 1 ][ i ], A[ 2 ][ i ], A[ 3 ][ i ] ) ) {					
				printf("Case #%d: O won\n", ct );
				newFlag = 0;
				break;
			}

		}

		if( newFlag ) {

			if( checkX( A[ 0 ][ 0 ], A[ 1 ][ 1 ], A[ 2 ][ 2 ], A[ 3 ][ 3 ] ) ) 					
				printf("Case #%d: X won\n", ct );

			else if( checkO( A[ 0 ][ 0 ], A[ 1 ][ 1 ], A[ 2 ][ 2 ], A[ 3 ][ 3 ] ) ) 								
				printf("Case #%d: O won\n", ct );

			else if( checkXT( A[ 0 ][ 0 ], A[ 1 ][ 1 ], A[ 2 ][ 2 ], A[ 3 ][ 3 ] ) ) 								
				printf("Case #%d: X won\n", ct );

			else if( checkOT( A[ 0 ][ 0 ], A[ 1 ][ 1 ], A[ 2 ][ 2 ], A[ 3 ][ 3 ] ) ) 							
				printf("Case #%d: O won\n", ct );
		
			else if( checkX( A[ 0 ][ 3 ], A[ 1 ][ 2 ], A[ 2 ][ 1 ], A[ 3 ][ 0 ] ) ) 								
				printf("Case #%d: X won\n", ct );

			else if( checkO( A[ 0 ][ 3 ], A[ 1 ][ 2 ], A[ 2 ][ 1 ], A[ 3 ][ 0 ] ) ) 
				printf("Case #%d: O won\n", ct );

			else if( checkXT( A[ 0 ][ 3 ], A[ 1 ][ 2 ], A[ 2 ][ 1 ], A[ 3 ][ 0 ] ) ) 
				printf("Case #%d: X won\n", ct );

			else if( checkOT( A[ 0 ][ 3 ], A[ 1 ][ 2 ], A[ 2 ][ 1 ], A[ 3 ][ 0 ] ) ) 
				printf("Case #%d: O won\n", ct );

			else if( flagVal )
				printf("Case #%d: Draw\n", ct );

			else
				printf("Case #%d: Game has not completed\n", ct );
		}			
			ct++;	
	}

	return 0;
}

