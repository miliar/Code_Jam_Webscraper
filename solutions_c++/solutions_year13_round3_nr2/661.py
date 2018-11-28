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
#define MAX_LENGTH 100100
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
    string s ;
    int x , y , dis ;
} ;

char done[ 1010 ][ 1010 ][ 510 ] , cc ;
int dx[] = { 0 , 0 , +1 , -1 } ;
int dy[] = { +1 , -1 , 0 , 0 } ;
char dd[] = { 'N' , 'S' , 'E' , 'W' } ;

int main() {
    freopen( "bs1.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	int T , res , n , i , ind , x , y , a , b , c , d , xe , ye , nx , ny ;
	st u , v ;
	string s , t , z ;
	scanf( "%d" , &T ) ;
	CLR( done ) ;
	cc = 1 ;
	fort( 1 , T ) {
	    cc++ ;
	    fprintf( stderr , "%d\n" , ind ) ;
		scanf( "%d" , &xe ) ;
		scanf( "%d" , &ye ) ;
		queue< st > que ;
		u.x = 0 ;
		u.y = 0 ;
		u.dis = 1 ;
		u.s = "" ;
		que.push( u ) ;
		done[ u.x + 500 ][ u.y + 500 ][ u.dis ] = cc ;
		z = "--" ;
		while( ! que.empty() ) {
            u = que.front() ;
            que.pop() ;
            //printf( "%d %d %d\n" , u.x , u.y , u.dis ) ;
            if( u.x == xe && u.y == ye ) {
                z = u.s ;
                break ;
            }
            fori( 4 ) {
                v.x = u.x + ( dx[ i ] * u.dis ) ;
                v.y = u.y + ( dy[ i ] * u.dis ) ;
                v.s = u.s + dd[ i ] ;
                v.dis = u.dis + 1 ;
                if( v.x >= -500 && v.x <= 500 && v.y >= -500 && v.y <= 500 && v.dis <= 500 ) {
                    if( done[ v.x + 502 ][ v.y + 502 ][ v.dis ] != cc ) {
                        done[ v.x + 502 ][ v.y + 502 ][ v.dis ] = cc ;
                        que.push( v ) ;
                    }
                }
            }
		}
		printf( "Case #%d: %s\n" , ind , z.c_str() ) ;
	}
	return 0 ;
}
