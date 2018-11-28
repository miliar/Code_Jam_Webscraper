/*
Author      : Mir Riyanul Islam
ID          : 
Name        : 
Judge       : 
Algorithm   : 
*/
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

#define fst first
#define scd second
#define pb push_back
#define psp() cout << " "
#define pnl() cout << endl
#define sq( x ) ( (x) * (x) ) 
#define phl() cout << "Hello World!!!"
#define pcase( x ) printf( "Case #%d:", (x) )
#define read( in ) freopen( (in), "r", stdin )
#define write( out ) freopen( (out), "w", stdout )
#define rep( i, a, b ) for( (i) = (a); (i) <= (b); (i)++ )
#define rev( i, a, b ) for( (i) = (a); (i) >= (b); (i)-- )
#define mems( arr, val ) memset( (arr), (val), sizeof( (arr) ) )

#define scan1( x ) cin >> (x)
#define scan2( x, y ) cin >> (x) >> (y)
#define scan3( x, y, z ) cin >> (x) >> (y) >> (z)

#define print1( x ) cout << (x)
#define print2( x, y ) cout << (x) << " " << (y)
#define print3( x, y, z ) cout << (x) << " " << (y) << " " << (z)

using namespace std;

typedef long long ll;
typedef queue <int> qi;
typedef vector <int> vi;
typedef map <int, int> mii;
typedef pair <int, int> pii;
typedef map <char, int> mci;
typedef map <string, int> msi;
typedef pair <string, int> psi;
typedef unsigned long long ull;
typedef map <string, string> mss;

template<class T>inline T SQ( T a ) { return a * a; }
template<class T>inline T MAX( T a, T b ) { return a > b ? a : b;  }
template<class T>inline T MIN( T a, T b ) { return a < b ? a : b;  }
template<class T>inline T ABS( T a ) { return a < 0 ? ( a * -1 ) : a; }
template<class T>inline void SWAP( T &a, T &b ) { a ^= b; b = a ^ b; a ^= b; }
template<class T>inline T GCD( T a, T b ) { while( b ) { b ^= a ^= b ^= a %= b; } return a; }
template<class T, class T1>inline void REVS( T1 &A, T i, T j ) { for( ; i < j; i++, j-- ) SWAP( A[i], A[j] ); }
template<class T, class T1>inline void REVC( T1 A[], T i, T j ) { for( ; i < j; i++, j-- ) SWAP( A[i], A[j] ); }

const int SZ = 1000006;
const double EPS = 1e-11;
const ll INF = 2147383647;
const ll MOD = 10000007;
const double PI = 2 * acos( 0.0 );

int vhx[] = { 0, -1, 0, 1 }, vhy[] = { -1, 0, 1, 0 };
int vhax[] = { 0, -1, -1, -1, 0, 1, 1, 1 }, vhay[] = { -1, -1, 0, 1, 1, 1, 0, -1 };

int main() {
    //ios_base::sync_with_stdio( 0 );
    //cin.tie( 0 );
    #define fileIO
    //#define deBug
    //#define cfTest
#ifdef fileIO
    read( "A-small-attempt0.in" );
    write( "A-small-attempt0.out" );
#endif
#ifdef cfTest
    while( 1 ) {
#endif
	
	int tc, cn = 0;
	scan1( tc );
	while( tc-- ) {
		int ans1, ans2, tmp[4], row1[4], row2[4], num[20];
		scan1( ans1 );
		int i, j;
		vi ans;
		mems( num , 0 );
		rep( i, 1, 4 ) {
			if( i == ans1 ) {
				rep( j, 0, 3 ) {
					scan1( row1[j] );
					num[row1[j]]++;
				}
			}
			else {
				rep( j, 0, 3 ) {
					scan1( tmp[j] );
				}
			}
		}
		scan1( ans2 );
		rep( i, 1, 4 ) {
			if( i == ans2 ) {
				rep( j, 0, 3 ) {
					scan1( row2[j] );
					if( num[row2[j]] > 0 ) {
						ans.pb( row2[j] );
					}
				}
			}
			else {
				rep( j, 0, 3 ) {
					scan1( tmp[j] );
				}
			}
		}
		pcase( ++cn ), psp();
		if( ans.size() == 0 ) {
			print1( "Volunteer cheated!" ), pnl();
		}
		else if( ans.size() == 1 ) {
			print1( ans[0] ), pnl();
		}
		else {
			print1( "Bad magician!" ), pnl();
		}
	}

#ifdef cfTest
    }
#endif
    
    return 0;
}