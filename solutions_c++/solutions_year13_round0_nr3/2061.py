#ifndef ALMACROS_H_INCLUDED
#define ALMACROS_H_INCLUDED

#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;
#define FOR( k, n ) for( int k = 0, gtrhr = ( int )n ; k < gtrhr ; ++k )
#define RFOR( k, n ) for( int k = ( int )n - 1 ; k >= 0 ; --k )

#define R_INT( x ) int x ; scanf( "%d", &x ) ;
#define R_ARRINTS( x, upper, actual ) int x[ actual ] ; for( int i = 0 ; i < actual ; ++i ) scanf( "%d", x + i ) ;
#define R_VECINTS( x, actual ) vector< int > x( actual, 0 ) ; for( int i = 0 ; i < actual ; ++i ) scanf( "%d", &( x[ i ] ) ) ;


#endif // ALMACROS_H_INCLUDED
