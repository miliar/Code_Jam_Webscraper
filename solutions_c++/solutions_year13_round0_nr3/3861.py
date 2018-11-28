
/*-------------------------------------------*/
//Author      : Mir Riyanul Islam (Riyan)  
//University  : AIUB                       
//E-mail      : mir_riyan@yahoo.com        
//Problem ID  : C                     
//Problem Name: Fair and Square
//Algorithm   : 
/*-------------------------------------------*/
#pragma comment( linker , "/STACK:16777216" )
#pragma warning( disable : 4786 )
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

//#define deBug
#define inOut

#define MS 111
#define pnl puts( "" )
#define psp cout << " "
#define lint long long int
#define prnt( a ) cout << a
#define phl cout << "Hello World!!!"
#define prntln( a ) cout << a << endl
#define prntD( a ) printf( "%.3lf" , a )

using namespace std;

const int INF = 1 << 30;
const double EPS = 1e-11;
const double PI = 2 * acos( 0.0 );

int MAX( int a , int b ) { return a > b ? a : b;  }
int MIN( int a , int b ) { return a < b ? a : b;  }
void SWAP( int &a , int &b ) { int t = a; a = b; b = t; }
int GCD( int a , int b ) { while( b ) { b ^= a ^= b ^= a %= b; } return a; }

bool isPalindrome( lint A ) {
	char num[100];
	int n , i = 0 , j;
	while( A > 0 ) {
		num[i] = ( A % 10 ) + '0';
		A /= 10;
		i++;
	}
	num[i] = 0;
	j = i - 1;
	i = 0;
	while( num[i] == num[j] && i <= j ) {
		i++;
		j--;
	}
	if( i > j ) return true;
	else return false;
}

int main() {

#ifdef inOut
	freopen( "C-small-attempt0.in" , "r" , stdin );
	freopen( "C-small-attempt0.out" , "w" , stdout );
#endif

	bool f1 , f2;
	int tc , cn = 0 , cnt;
	lint a , b , sqrtA , i , sqI;
	scanf( "%d" , &tc );
	while( tc-- ) {
		scanf( "%lld %lld" , &a , &b );
		sqrtA = lint( sqrt( double( a ) ) );
		for( i = sqrtA , cnt = 0 ; i * i <= b ; i++ ) {
			sqI = i * i;
			if( sqI >= a ) {
				f1 = isPalindrome( i );
				f2 = isPalindrome( sqI );
				if( f1 && f2 ) cnt++;
			}
		}
		printf( "Case #%d: %d\n" , ++cn , cnt );

#ifdef deBug
		
#endif

	}

	return 0;

}

