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

lll arr[ MAX_LENGTH ] , brr[ MAX_LENGTH ] ;
set< lll > S ;
set< lll > :: iterator it , it2 ;

void insert( lll a ) {
    if( S.find( a ) == S.end() ) {
        brr[ a ] = 1 ;
        S.insert( a ) ;
    }
    else {
        brr[ a ]++ ;
    }
}

void delet( lll a ) {
    brr[ a ]-- ;
    if( ! brr[ a ] ) {
        it2 = S.find( a ) ;
        S.erase( it2 ) ;
    }
}

int main() {
    freopen( "al.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	lll T , res , n , i , ind , a , b , j , c , d , e ;
	bool fl ;
	scanf( "%lld" , &T ) ;
	fort( 1 , T ) {
	    CLR( brr ) ;
	    S.clear() ;
	    fprintf( stderr , "%lld\n" , ind ) ;
        scanf( "%lld" , &a ) ;
		scanf( "%lld" , &n ) ;
		fori( n ) {
		    scanf( "%lld" , &arr[ i ] ) ;
		}
		sort( arr , arr + n ) ;
		res = ( 1LL << 62LL ) ;
        fori( n + 1 ) {
            b = a ;
            fl = 1 ;
            d = 0 ;
            forj( i ) {
                if( arr[ j ] < b ) {
                    b += arr[ j ] ;
                }
                else {
                    c = b ;
                    if( c == 1 ) {
                        fl = 0 ;
                        break ;
                    }
                    while( 1 ) {
                        d++ ;
                        c += c - 1 ;
                        if( arr[ j ] < c ) {
                            break ;
                        }
                    }
                    b = c + arr[ j ] ;
                }
            }
            d += n - i ;
            if( fl ) {
                res = MIN( res , d ) ;
            }
        }
		printf( "Case #%lld: %lld\n" , ind , res ) ;
	}
	return 0 ;
}
