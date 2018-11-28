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

//const int RNG = 1004;
const int SIZ = 1004;
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

int preRes[ SIZ ];

bool isPalindrome( int n ) {
	int res = 1, rem; int k=0;
	char arr[ 25 ];
	mset( arr, 0 );
	while( res != 0 ) {
		res = n/10;
		rem = n%10;
		n = res;
		arr[k++] = (char)(rem+'0');
	}
	int len = strlen( arr );
	int i, j;
	for( i=0,j=len-1; i<=j; i++,j-- ) {
		if( arr[i] == arr[j] ) continue;
		else break;
	}
	if( i > j ) return true;
	else return false;
}

void preCalc( ) {
	int tmp;
	int i;
	for( i=1; i<SIZ; i++ ) {
		tmp = i*i;
		if( tmp > SIZ ) break;
		if( isPalindrome(i) && isPalindrome(tmp) )
			preRes[tmp] = 1;
	}
	for( i=1; i<SIZ; i++ ) preRes[i] += preRes[i-1];
}

int main( ){
	#define DeBug
	#ifdef DeBug
		READ( "C-small-attempt0.in" );
		WRITE( "C-small-attempt0.out" );
	#endif
	preCalc( );
	int TC, caseno = 1;
	scanf( "%d", &TC );
	while( TC-- ) {
		int a, b;
		scanf( "%d %d", &a, &b );
		printf( "Case #%d: ", caseno++ );
		printf( "%d\n", preRes[b]-preRes[a-1] );
	}
	return 0;
}
