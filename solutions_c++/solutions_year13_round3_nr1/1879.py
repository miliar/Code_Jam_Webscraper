#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define MAXN 111

char text[MAXN];
int T, n, len, maxu;

bool consonant( char tmp ) {

     if ( tmp == 'a' || tmp == 'e' || tmp == 'i' || tmp == 'o' || tmp == 'u' )
        return ( false );
     
     return ( true );
     
}

int main( ) {

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    cin >> T;//scanf ( "%d", &T );
    
    for ( int t = 1; t <= T; ++t ) {
    
        cin >> text >> n;//scanf ( " %s %d", text, n );
        
        len = strlen( text );
        
        long long sol = 0;
        
        for ( int i = 1; i <= len; ++i )
            for ( int j = 1; j <= len; ++j ) {
            
                int sum = 0;
            
                for ( int k = i; k <= j; ++k )
                    if ( consonant( text[k-1] ) ) {
                       ++sum;
                       if ( sum == n ) {
                          ++sol;
                          k = j+1;
                       }
                    }else {
                       sum = 0;
                    }
                    
            }
        
        printf ( "Case #%d: %lld\n", t, sol ); 
        
    }

    return 0;
   
}
