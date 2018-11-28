#include <stdio.h>

int main( void ) {
     int a, b, k;
     int nCase, n = 1;
     
     scanf("%i", &nCase);
     
     while( nCase-- ) {
          scanf("%i %i %i", &a, &b, &k);
          
          int ans = 0;
          for( int i = 0; i < a; i++ )
               for( int j = 0; j < b; j++ )
                    if( (i & j) < k ) ans++;
          
          printf("Case #%i: %i\n", n++, ans);
     }
     
     return 0;
}
