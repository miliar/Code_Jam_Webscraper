#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

#define MAXN 1000

struct state {
       int val;       
};

state node[4*MAXN];

bool F[MAXN+1];
int T, A, B;

void build( int v, int begin, int end ) {

     if ( begin == end ) {
        node[v].val = F[begin];
        return;
     }
     
     int mid = ( begin+end ) / 2;
     
     build( 2*v, begin, mid );
     build( 2*v+1, mid+1, end );
     
     node[v].val = node[2*v].val + node[2*v+1].val;
     
}

state query( int v, int x, int y, int qx, int qy ) {

      if ( x == qx && y == qy )
         return ( node[v] );
      
      int mid = ( x + y ) / 2;
      
      if ( qy <= mid ) {
         return ( query( 2*v, x, mid, qx, qy ) );    
      }else if ( qx > mid ) {
         return ( query( 2*v+1, mid+1, y, qx, qy ) );
      }else {
         state q1 = ( query( 2*v, x, mid, qx, mid ) );
         state q2 = ( query( 2*v+1, mid+1, y, mid+1, qy ) );
         state ret;
         ret.val = q1.val + q2.val;
         return ( ret );     
      }
      
}

int palindrome( int n ) {
     
     int ret = 0;
     
     while ( n > 0 ) {
           ret *= 10;
           ret += (n % 10);
           n /= 10;
     }
     
     return ( ret );
     
}

int main( ) {

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    for ( int i = 1; i <= MAXN; ++i ) {
        if ( i == palindrome(i) && i*i == palindrome(i*i) && (i*i) <= MAXN )
           F[i*i] = 1;
    }

    build( 1, 1, MAXN );

    scanf ( "%d", &T );
    
    for ( int t = 1; t <= T; ++t ) {
    
        scanf ( "%d %d", &A, &B );
        
        printf ( "Case #%d: %d\n", t, query( 1, 1, MAXN, A, B ).val );
        
    }

    return 0;
   
}
