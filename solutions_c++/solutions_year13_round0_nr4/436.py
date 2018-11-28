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

#define MAX_SIZE 2100000
#define MAX_LENGTH 220
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

struct st {
    vector< int > adj ;
    int t ;
} brr[ MAX_LENGTH ] ;

int hand[ MAX_LENGTH ] , done[ 1 << 22 ] , LIM , cc ;
bool memo[ 1 << 22 ] ;
vector< int > adj_list[ MAX_SIZE ] , res_adj ;

void precal( int n ) {
    int i , lim , a , sz , j , k , mask ;
    lim = 1 << n ;
    fori( lim ) {
        mask = i ;
        CLR( hand ) ;
        forj( n ) {
            if( ( mask & ( 1 << j ) ) != 0 ) {
                sz = brr[ j ].adj.size() ;
                for( k = 0 ; k < sz ; k++ ) {
                    a = brr[ j ].adj[ k ] ;
                    hand[ a ]++ ;
                }
                if( brr[ j ].t != -1 ) {
                    hand[ brr[ j ].t ]-- ;
                }
            }
        }
        forj( n ) {
            if( ( mask & ( 1 << j ) ) == 0 ) {
                if( hand[ brr[ j ].t ] ) {
                    adj_list[ mask ].push_back( j ) ;
                }
            }
        }
    }
}

bool dp( int mask ) {
    if( mask == LIM ) {
        return 1 ;
    }
    bool &ret = memo[ mask ] ;
    int &re = done[ mask ] ;
    if( re == cc ) {
        return ret ;
    }
    re = cc ;
    bool res ;
    int i , sz , a ;
    res = 0 ;
    sz = adj_list[ mask ].size() ;
    fori( sz ) {
        a = adj_list[ mask ][ i ] ;
        res |= dp( mask | ( 1 << a ) ) ;
    }
    return ret = res ;
}

void path_print( int mask ) {
    if( mask == LIM ) {
        return ;
    }
    bool res ;
    int i , sz , a ;
    res = 0 ;
    sz = adj_list[ mask ].size() ;
    fori( sz ) {
        a = adj_list[ mask ][ i ] ;
        res |= dp( mask | ( 1 << a ) ) ;
        if( res ) {
            res_adj.push_back( a ) ;
            path_print( mask | ( 1 << a ) ) ;
            return ;
        }
    }
}

int main() {
    freopen( "ds4.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	int T , res , n , i , ind , j , a , cn , b , k ;
	scanf( "%d" , &T ) ;
	cc = 1 ;
	CLR( done ) ;
	fort( 1 , T ) {
	    cc++ ;
	    fprintf( stderr , "running case: %d\n" , ind ) ;
	    fori( MAX_LENGTH ) { brr[ i ].adj.clear() ; }
	    res_adj.clear() ;
        scanf( "%d" , &k ) ;
		scanf( "%d" , &n ) ;
		cn = 0 ;
		fori( k ) {
		    scanf( "%d" , &a ) ;
		    brr[ cn ].adj.push_back( a ) ;
		}
		brr[ cn ].t = -1 ;
		cn++ ;
		fori( n ) {
		    scanf( "%d" , &brr[ cn ].t ) ;
		    scanf( "%d" , &a ) ;
		    forj( a ) {
		        scanf( "%d" , &b ) ;
		        brr[ cn ].adj.push_back( b ) ;
		    }
		    cn++ ;
		}
		fori( MAX_SIZE ) { adj_list[ i ].clear() ; }
		precal( cn ) ;
		LIM = ( 1 << cn ) - 1 ;
		MEM( memo ) ;
        res = dp( 1 ) ;
        if( ! res ) {
            printf( "Case #%d: IMPOSSIBLE\n" , ind ) ;
        }
        else {
            path_print( 1 ) ;
            printf( "Case #%d:" , ind ) ;
            fori( res_adj.size() ) {
                printf( " %d" , res_adj[ i ] ) ;
            }
            printf( "\n" ) ;
        }
	}
	return 0 ;
}
