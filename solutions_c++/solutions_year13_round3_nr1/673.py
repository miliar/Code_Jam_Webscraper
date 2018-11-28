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
#define MAX_LENGTH 1000100
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

char arr[ MAX_LENGTH ] ;
lll N ;

struct st {
    lll l , h , v , z ;
} Tr[ 6 * MAX_LENGTH ] ;

void build( lll l , lll h , lll in ) {
    if( l == h ) {
        Tr[ in ].l = l ;
        Tr[ in ].h = h ;
        Tr[ in ].v = 0 ;
        Tr[ in ].z = l ;
        return ;
    }
    lll m = ( l + h ) / 2 ;
    build( l , m , 2 * in ) ;
    build( m + 1 , h , 2 * in + 1 ) ;
    Tr[ in ].l = l ;
    Tr[ in ].h = h ;
    Tr[ in ].v = 0 ;
    Tr[ in ].z = ( 1LL << 60LL ) ;
}

void update( lll l , lll h , lll in , lll a ) {
    lll tl = Tr[ in ].l ;
    lll th = Tr[ in ].h ;
    lll m = ( tl + th ) / 2 ;
    if( l == tl && h == th ) {
        Tr[ in ].v = a ;
        return ;
    }
    if( h <= Tr[ 2 * in ].h ) {
        update( l , h , 2 * in , a ) ;
    }
    else {
        update( l , h , 2 * in + 1 , a ) ;
    }
    Tr[ in ].v = MAX( Tr[ 2 * in ].v , Tr[ 2 * in + 1 ].v ) ;
    if( Tr[ 2 * in ].v >= N ) {
        Tr[ in ].z = Tr[ 2 * in ].z ;
    }
    else if( Tr[ 2 * in + 1 ].v >= N ) {
        Tr[ in ].z = Tr[ 2 * in + 1 ].z ;
    }
}

lll search( lll l , lll h , lll in ) {
    lll tl = Tr[ in ].l ;
    lll th = Tr[ in ].h ;
    lll m = ( tl + th ) / 2 ;
    lll x ;
    if( Tr[ in ].z == ( 1LL << 60LL ) || Tr[ in ].v < N ) {
        return ( 1LL << 60LL ) ;
    }
    if( tl == l && h == th ) {
        return Tr[ in ].z ;
    }
    if( h <= Tr[ 2 * in ].h ) {
        return search( l , h , 2 * in ) ;
    }
    else if( l >= Tr[ 2 * in + 1 ].l ) {
        return search( l , h , 2 * in + 1 ) ;
    }
    else {
        return MIN( search( l , m , 2 * in ) , search( m + 1 , h , 2 * in + 1 ) ) ;
    }
    return ( 1LL << 60LL ) ;
}

int main() {
    freopen( "al.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	lll T , res , n , i , ind , a , b , c , d , len ;
	scanf( "%lld" , &T ) ;
	fort( 1 , T ) {
	    scanf( "%s" , &arr ) ;
	    len = strlen( arr ) ;
		scanf( "%lld" , &n ) ;
		N = n ;
		a = 0 ;
		build( 1 , len , 1 ) ;
		for( i = len - 1 ; i >= 0 ; i-- ) {
            if( arr[ i ] == 'a' || arr[ i ] == 'e' || arr[ i ] == 'i' || arr[ i ] == 'o' || arr[ i ] == 'u' ) {
                a = 0 ;
            }
            else {
                a++ ;
            }
            update( i + 1 , i + 1 , 1 , a ) ;
            //print2( i + 1 , a ) ;
		}
		res = 0 ;
		fori( len ) {
		    a = search( i + 1 , len , 1 ) ;
		    //printf( "%lld %lld %lld\n" , i + 1 , len , a ) ;
		    if( a != -1 && a != ( 1LL << 60LL ) ) {
                res += len - ( a + n - 1 ) + 1 ;
		    }
		}
		printf( "Case #%lld: %lld\n" , ind , res ) ;
	}
	return 0 ;
}
