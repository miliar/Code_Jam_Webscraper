#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1005;

char S[ N ];
int global, n;
FILE* fin = fopen("a_in.txt", "r");
FILE* fout = fopen("a_out.txt", "w");

void load( ) {
	fscanf( fin, "%d", &n );
	n++;
	fscanf( fin, "%s", S );
}

void solve( ) {
	int active = S[ 0 ] - '0';
	int sol = 0;
	for( int i = 1; i < n; i++ ) {
			if( active >= i ) {
					active += S[ i ] - '0';
					continue;
			}
			sol += i - active;
			active += i - active + S[ i ] - '0';
	}
	fprintf( fout, "Case #%d: %d\n", ++global, sol );
}

int main( void ) {
	int t;
	fscanf( fin, "%d", &t );
	for( ; t; t-- ) {
			load( );
			solve( );
	}
	fclose( fin );
	fclose( fout );

	return 0;
}


