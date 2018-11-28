#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <queue>
#include <cassert>
#include <cmath>
#include <bitset>
#include <ctime>
#include <queue>
#include <fstream>
using namespace std;
 
#define pb push_back
#define mp make_pair
#define pii pair< int, int >
#define GC getchar( )
#define PC putchar
#define x first
#define y second

typedef long long llint;

FILE *fin = fopen( "input.txt", "r" );
FILE *fout = fopen( "output.txt", "w" );

int r, c, w;
int global;

void load( ) {
	fscanf( fin, "%d%d%d", &r, &c, &w );

}

void solve( ) {
	int sol = 0;
	int curr = c;
	while( curr >= w + 1 ) {
		curr -= w;
		sol++;
	}
	sol += w;
	fprintf( fout, "Case #%d: %d\n", ++global, sol * r );
		
}

	    
int main( void ) {
	int t;
	fscanf( fin, "%d", &t );
	while( t-- ) {
		load( );
		solve( );
	}
    return 0;
}
