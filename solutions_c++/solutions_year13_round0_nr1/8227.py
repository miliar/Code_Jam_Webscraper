/*
NAME : 	Md. Nabid Imteaj
PROB :
LANG : C/C++
*/
#pragma comment(linker, "/STACK:16777216")
#pragma warning(disable:4786)

#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <cctype>
#include <cassert>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

const int SIZ = 1000006;
const int INF = (1<<30);
const double PI = 2*acos(0.0);
const double EPS = 1e-11;

#define sq(x) ((x)*(x))
#define mset(x,n) memset((x),(n),sizeof((x)))

// debug
// courtesy: smilitude
#define D(x) if(1) cout << __LINE__ << " " << #x" = " << (x) << endl
#define D2(x,y) if(1) cout << __LINE__ << " " << #x" = " << (x) \
		<< ", " << #y" = " << (y) << endl
#define pfl(x) cout << (x) << endl
#define pf(x) cout << (x)
#define pfln() cout << endl
#define pfs() cout << " "
#define READ(f) freopen( f, "r", stdin )
#define WRITE(f) freopen( f, "w", stdout )
#define Sys() system( "pause" )

#define REP(i,n) for( int i=0,_e(n); i<_e; i++ )
#define FOR(i,a,b) for( int i=(a),_e(b); i<=_e; i++ )

//template<class T> T BitLen( T a ){ return (1+(floor(log(a)))); }// Note: return bit length of a number [alternate ceil(1+log(a));]
template<class T>inline T MAX( T a, T b ){ return a>b ? a:b; } // Note: returns maximum of a and b
template<class T>inline T MIN( T a, T b ){ return a<b ? a:b; } // Note: returns minimum of a and b
//template<class T>inline T GCD( T a, T b ){ if(a<0)return GCD(-a,b); if(b<0)return GCD(a,-b);while(b){ b^=a^=b^=a%=b; }return a; } // Note: returns GCD of a and b
//template<class T>inline T LCM( T a, T b ){ if(a<0)return LCM(-a,b); if(b<0)return LCM(a,-b);return a/GCD(a,b)*b; } // Note: returns LCM of a and b
template<class T>inline void SWAP( T &a, T &b ) { a = a^b; b = a^b; a = a^b; } // Note: swaps a to b, *Not for Double
//inline void SWAP(double &a, double &b) { double c = a; a = b; b = c;} // Note: swaps a to b *Double
//template<class T, class T1>T Reverse( T1 A[], T i, T j ) { for(i,j-=1; i<j; i++, j--) SWAP(A[i], A[j]); return 0;} // Note: char array reverse form i to j
//template<class T, class T1>T Reverse( T1 &A, T i, T j ) { for(i,j-=1; i<j; i++, j--) SWAP(A[i], A[j]); return 0;} // Note: string reverse
//template< class T >inline T fAbs( T a ) { return a<0 ? (a*(-1)) : a; }

char arr[5][5];

int winnerChk( ) { // brute force
	int x_cnt, o_cnt, dot_cnt, i, j;
	x_cnt = o_cnt = dot_cnt = 0;
	// diagonal checking
	for( i=0; i<4; i++ ) {
		if( arr[i][i] == 'X' ) x_cnt++;
		else if( arr[i][i] == 'O' ) o_cnt++;
		else if( arr[i][i] == 'T' ) x_cnt++, o_cnt++;
		else if( arr[i][i] == '.' ) dot_cnt++;
	}
	if( x_cnt == 4 ) return 1; // x
	else if( o_cnt == 4 ) return 2; // o
	x_cnt = o_cnt = dot_cnt = 0;
	for( i=0,j=3; i<4; i++,j-- ) {
		if( arr[i][j] == 'X' ) x_cnt++;
		else if( arr[i][j] == 'O' ) o_cnt++;
		else if( arr[i][j] == 'T' ) x_cnt++, o_cnt++;
		else if( arr[i][j] == '.' ) dot_cnt++;
	}
	if( x_cnt == 4 ) return 1; // x
	else if( o_cnt == 4 ) return 2; // o
	x_cnt = o_cnt = dot_cnt = 0;
	// row checking
	for( i=0; i<4; i++ ) {
		x_cnt = o_cnt = dot_cnt = 0;
		for( j=0; j<4; j++ ) {
			if( arr[i][j] == 'X' ) x_cnt++;
			else if( arr[i][j] == 'O' ) o_cnt++;
			else if( arr[i][j] == 'T' ) x_cnt++, o_cnt++;
			else if( arr[i][j] == '.' ) dot_cnt++;
		}
		if( x_cnt == 4 ) return 1; // x
		else if( o_cnt == 4 ) return 2; // o
	}
	// column cheking
	for( i=0; i<4; i++ ) {
		x_cnt = o_cnt = dot_cnt = 0;
		for( j=0; j<4; j++ ) {
			if( arr[j][i] == 'X' ) x_cnt++;
			else if( arr[j][i] == 'O' ) o_cnt++;
			else if( arr[j][i] == 'T' ) x_cnt++, o_cnt++;
			else if( arr[j][i] == '.' ) dot_cnt++;
		}
		if( x_cnt == 4 ) return 1; // x
		else if( o_cnt == 4 ) return 2; // o
	}
	if( dot_cnt == 0 ) return 3; // draw
	else return 0; // not completed
}

int main( ){
	#define DeBug
	#ifdef DeBug
		READ( "A-small-attempt0.in" );
		WRITE( "A-small-attempt0.out" );
	#endif
	int TC, caseno = 1;
	scanf( "%d", &TC );
	while( TC-- ) {
		mset( arr, 0 );
		int i;
		for( i=0; i<4; i++ ) scanf( "%s", arr[i] );
		int tmp = winnerChk( );
		printf( "Case #%d: ", caseno++ );
		if( tmp == 1 ) printf( "X won" );
		else if( tmp == 2 ) printf( "O won" );
		else if( tmp == 3 ) printf( "Draw" );
		else printf( "Game has not completed" );
		printf( "\n" );
	}
	return 0;
}
