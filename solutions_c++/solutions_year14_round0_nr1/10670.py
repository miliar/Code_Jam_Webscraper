/*
Name: Md. Nabid Imteaj
Prob:
Lang: C/C++
*/

#pragma comment( linker, "/STACK:16777216" )
#pragma warning( disable:4786 )

#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

// debug
// credit: smilitude
#define D(x) if(1) cout << __LINE__ << " " << #x" = " << (x) << endl
#define D2(x,y) if(1) cout << __LINE__ << " " << #x" = " << (x) \
			   << ", " << #y" = " << (y) << endl
#define READ(f) freopen( (f), "r", stdin )
#define WRITE(f) freopen( (f), "w", stdout )
#define pf(x) cout << (x)
#define pfl(x) cout << (x) << endl
#define pfln() cout << endl
#define pfs() cout << " "
#define FOR(i,a,b) for(int i=(a),_e(b); i<=_e; i++)
#define REP(a,b) for(int i=(a),_e(b); i<_e; i++)
#define mset(x,n) memset((x), (n), sizeof((x)))

template<class T> inline T MAX( T a, T b ) { return a>b?a:b; }
template<class T> inline T MIN( T a, T b ) { return a<b?a:b; }
template<class T> inline void SWAP( T &a, T &b ) { a=a^b; b=a^b; a=a^b; }
template<class T, class T1>inline void Reverse( T1 A[], T i, T j ) { for( ; i<j; i++,j-- ) SWAP( A[i], A[j] ); }
template<class T> inline T fAbs( T a ) { return a<0?a*(-1):a; }

const int sz = 20;
const int inf = 1<<29;
const double PI = 2*acos(0.0);
const double eps = 1e-9;

int vis[sz];

int main( ) {
  #define DeBug
	#ifdef DeBug
		READ( "input.in" );
		WRITE( "output.out" );
	#endif

	int tc, caseno = 1;
	scanf( "%d", &tc );
	while( tc-- ) {
		int a1, a2, tmp;
		scanf( "%d", &a1 );
		int i, j;
		mset( vis, 0 );
		for( i=1; i<=4; i++ ) {
			for( j=1; j<=4; j++ ) {
				scanf( "%d", &tmp );
				if( i == a1 ) vis[ tmp ] ++;
			}
		}

		scanf( "%d", &a2 );
		for( i=1; i<=4; i++ ) {
			for( j=1; j<=4; j++ ) {
				scanf( "%d", &tmp );
				if( i == a2 ) vis[ tmp ] ++;
			}
		}

		tmp = 0;
		for( i=1; i<=16; i++ ) if( vis[i] == 2 ) { j = i; tmp++; }

		printf( "Case #%d: ", caseno++ );
		if( tmp == 1 ) {
			printf( "%d\n", j );
		} else if( tmp == 0 ) {
			puts("Volunteer cheated!");
		} else {
			puts("Bad magician!");
		}
	}

	return 0;
}
