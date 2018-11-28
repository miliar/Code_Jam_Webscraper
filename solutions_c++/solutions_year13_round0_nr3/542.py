#pragma comment(linker, "/STACK:16777216")
#pragma warning(disable:4786)

#include <set>
#include <map>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <ctime>
#include <bitset>
#include <vector>
#include <cstdio>
#include <cctype>
#include <string>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <numeric>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define MAX_SIZE 100100
#define MAX_LENGTH 10000100
#define INF ( 1 << 29 )

#define CLR( a ) memset( a , NULL , sizeof( a ) )
#define MEM( a ) memset( a , -1 , sizeof( a ) )
#define fort( a , b ) for( ind = ( a ) ; ind <= ( b ) ; ind++ )
#define foriab( a , b ) for( i = ( a ) ; i < ( b ) ; i++ )
#define fori( a ) for( i = 0 ; i < ( a ) ; i++ )
#define forj( a ) for( j = 0 ; j < ( a ) ; j++ )
#define print1( a ) printf( "%lld ---\n" , ( a ) )
#define print2( a , b ) printf( "%lld %lld ---\n" , ( a ) , ( b ) )

typedef long long lll ;

lll MIN( lll a , lll b ) { return a < b ? a : b ; }
lll MAX( lll a , lll b ) { return a > b ? a : b ; }
lll GCD( lll a , lll b ) { while( b ) b ^= a ^= b ^= a %= b ; return a ; }
lll LCM( lll a , lll b ) { return a * ( b / GCD( a , b ) ) ; }
void SWAP( lll &a , lll &b ) { a = a ^ b ; b = a ^ b ; a = a ^ b ; }

const double PI = acos( -1 ) ;
const double EPS = 1e-11 ;

lll brr[ MAX_LENGTH ] ;

bool isP( lll a ) {
    lll arr[ 30 ] ;
    lll cn , fl , i , j ;
    cn = 0 ;
    fl = 1 ;
    while( a ) {
        arr[ cn++ ] = a % 10 ;
        a /= 10 ;
    }
    reverse( arr , arr + cn ) ;
    j = cn - 1 ;
    fori( cn ) {
        if( arr[ i ] != arr[ j ] ) {
            fl = 0 ;
            break ;
        }
        if( i > j ) {
            break ;
        }
        j-- ;
    }
    return fl ;
}

int main() {
    freopen( "cl1.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	lll T , res , n , i , ind , a , b , c , d , j , e , f , lim ;
	lim = 1e7 ;
	CLR( brr ) ;
	for( i = 1 ; i <= lim ; i++ ) {
        if( isP( i ) && isP( i * i ) ) {
            brr[ i ]++ ;
        }
    }
    for( i = 1 ; i <= lim ; i++ ) {
        brr[ i ] += brr[ i - 1 ] ;
    }
	scanf( "%lld" , &T ) ;
	fort( 1 , T ) {
		scanf( "%lld" , &a ) ;
		scanf( "%lld" , &b ) ;
        c = ( lll ) ( sqrt( ( double ) a ) + EPS ) ;
        d = ( lll ) ( sqrt( ( double ) b ) + EPS ) ;
        if( c * c != a ) { c++ ; }
		res = brr[ d ] - brr[ c - 1 ] ;
		printf( "Case #%lld: %lld\n" , ind , res ) ;
	}
	return 0 ;
}
