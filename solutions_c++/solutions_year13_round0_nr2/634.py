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
#define MAX_LENGTH 110
#define INF ( 1 << 29 )

#define CLR( a ) memset( a , NULL , sizeof( a ) )
#define MEM( a ) memset( a , -1 , sizeof( a ) )
#define fort( a , b ) for( ind = ( a ) ; ind <= ( b ) ; ind++ )
#define foriab( a , b ) for( i = ( a ) ; i < ( b ) ; i++ )
#define fori( a ) for( i = 0 ; i < ( a ) ; i++ )
#define forj( a ) for( j = 0 ; j < ( a ) ; j++ )
#define print1( a ) printf( "%d ---\n" , ( a ) )
#define print2( a , b ) printf( "%d %d ---\n" , ( a ) , ( b ) )

typedef long long lll ;

int MIN( int a , int b ) { return a < b ? a : b ; }
int MAX( int a , int b ) { return a > b ? a : b ; }
int GCD( int a , int b ) { while( b ) b ^= a ^= b ^= a %= b ; return a ; }
int LCM( int a , int b ) { return a * ( b / GCD( a , b ) ) ; }
void SWAP( int &a , int &b ) { a = a ^ b ; b = a ^ b ; a = a ^ b ; }

const double PI = acos( -1 ) ;
const double EPS = 1e-11 ;

int arr[ MAX_LENGTH ][ MAX_LENGTH ] ;

int main() {
    freopen( "bl.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	int T , res , n , i , j , m , ind , a , b , c , k ;
	scanf( "%d" , &T ) ;
	fort( 1 , T ) {
        CLR( arr ) ;
		scanf( "%d" , &n ) ;
		scanf( "%d" , &m ) ;
		fori( n ) {
		    forj( m ) {
		        scanf( "%d" , &arr[ i ][ j ] ) ;
		    }
		}
		res = 1 ;
		fori( n ) {
		    forj( m ) {
		        a = arr[ i ][ j ] ;
		        b = 1 ;
		        for( k = 0 ; k < m ; k++ ) {
                    if( arr[ i ][ k ] > a ) {
                        b = 0 ;
                        break ;
                    }
		        }
		        if( b ) { continue ; }
		        b = 1 ;
		        for( k = 0 ; k < n ; k++ ) {
                    if( arr[ k ][ j ] > a ) {
                        b = 0 ;
                        break ;
                    }
		        }
		        if( b ) { continue ; }
		        if( ! b ) {
                    res = 0 ;
                    break ;
                }
		    }
		    if( ! res ) { break ; }
		}
		if( res ) {
            printf( "Case #%d: YES\n" , ind ) ;
		}
		else {
            printf( "Case #%d: NO\n" , ind ) ;
		}
	}
	return 0 ;
}
