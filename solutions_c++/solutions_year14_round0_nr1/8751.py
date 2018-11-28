#include <cstdio>

using namespace std;

int T, R1, R2;
int M1[5][5], M2[5][5];

void solve( int t ) {
	
	scanf( "%d", &R1 ); --R1;
	for ( int i = 0; i < 4; ++i ) 
		for ( int j = 0; j < 4; ++j ) 
			scanf( "%d", &M1[i][j] );
			
	scanf( "%d", &R2 ); --R2;
	for ( int i = 0; i < 4; ++i ) 
		for ( int j = 0; j < 4; ++j ) 
			scanf( "%d", &M2[i][j] );
	
	int pivot = -1, cnt = 0;
	for ( int i = 0; i < 4; ++i ) {
		for ( int j = 0; j < 4; ++j ) {
			if ( M1[R1][i] == M2[R2][j] ){ pivot = i; ++cnt; }
		}
	} 
	
	printf( "Case #%d: ", t );
	
	if ( cnt == 0 ) { printf( "Volunteer cheated!\n" ); return; }
	if ( cnt > 1 ) { printf( "Bad magician!\n" ); return; }
	
	printf( "%d\n", M1[R1][pivot] );
	
}

int main( void ) {

	scanf( "%d", &T );
	for ( int i = 0; i < T; ++i ) solve( i + 1 );
	
	return 0;

}
