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
 
typedef long long llint;
 
const int N = 1000005;

//2 -> i, 3 -> j, 4 -> k

FILE *fin = fopen( "b_in.txt", "r" );
FILE *fout = fopen( "b_out.txt", "w" );

int l, x;
int global;
char S[ N ];
int SUFF[ N ];
int cnt;

int M[ 5 ][ 5 ] = { { 0, 0, 0, 0 }, { 0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 }, { 0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };

void load( ) {
	fscanf( fin, "%d%d", &l, &x );
	fscanf( fin, "%s", S );
	cnt = l;
	for( int i = 0; i < x-1; i++ ) {
		for( int j = 0; j < l; j++ ) {
			S[ cnt++ ] = S[ j ];
		}
	}
}

int f( char a ) {
	if( a == 'i' ) return 2;
	if( a == 'j' ) return 3;
	return 4;
}

void solve( ) {
	SUFF[ cnt ] = 1;
	for( int i = 0; i < cnt; i++ ) {
		int go = 1;
		for( int j = i; j < cnt; j++ ) {
			bool ff = false;
			if( go < 0 ) go *= -1, ff = true;
			go = M[ go ][ f( S[ j ] ) ];
			if( ff ) go *= -1;
		}
		SUFF[ i ] = go;
	}
	int go = 1;
	bool da = false;
	for( int i = 0; i < cnt; i++ ) {
		bool ff = false;
		if( go < 0 ) go *= -1, ff = true;
		go = M[ go ][ f( S[ i ] ) ];
		if( ff ) go *= -1;
		if( go != 2 ) continue;
		int go2 = 1;
		for( int j = i + 1; j < cnt - 1; j++ ) {
			bool ff = false;
			if( go2 < 0 ) go2 *= -1, ff = true;
			go2 = M[ go2 ][ f( S[ j ] ) ];
			if( ff ) go2 *= -1;
			if( go2 != 3 ) continue;
			if( SUFF[ j + 1 ] != 4 ) continue;
			da = true;
			if( da ) break;
		}
		if( da ) break;
	}
	fprintf( fout, "Case #%d: %s\n", ++global, da ? "YES" : "NO" );
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
	
































