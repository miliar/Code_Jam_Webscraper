#include <cstdio>
#include <cstring>
#include <fstream>
#include <cmath>

#define MAXN 10000010

FILE *fin = fopen( "Cin.txt", "r" );
FILE *fout = fopen( "Cout.txt", "w" );

using namespace std;

int T;
int niz[MAXN];

long long A, B;

inline bool check_pal( long long x ){
	
	char s[25];
	sprintf( s, "%lld", x ); int len = strlen ( s );
	
	for ( int i = 0; i < len; ++i ){
		if ( s[i] != s[len - i - 1] ) return false;
	}
	
	return true;
	
}

inline int init(){

	niz[0] = 0;
	for ( int i = 1; i <= 10000000; ++i ){
		niz[i] = niz[i - 1] + ( check_pal( (long long) i ) && check_pal ( (long long) i * i ) );
	}

}

int main( void ){

	init();
	
	fscanf( fin, "%d", &T );
	for ( int i = 0; i < T; ++i ){
		
		fscanf( fin, "%lld%lld", &A, &B );
		
		long long a = (long long) sqrt( A ), b = (long long) sqrt( B );
		if ( a * a != A ) ++a;
		
		fprintf( fout, "Case #%d: %d\n", i + 1, niz[b] - niz[a - 1] );
	}
		
	return 0;
	
	
}