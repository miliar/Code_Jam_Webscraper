#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

#define MAXN 1005

using namespace std;

int t, Smax, ans, people_up;
char text[MAXN];

int main( ) {

    scanf( "%d", &t );
    
    for ( int T = 0; T < t; ++T ) {
    
        ans = 0;
        
        scanf( "%d %s", &Smax, text );
    
        people_up = text[0]-'0';
    
        for ( int i = 1; text[i] != '\0'; ++i ) {
            if ( people_up < i ) {
                ans += i - people_up;
                people_up += i - people_up;
            }
            people_up += text[i]-'0';
        }
        
    
        printf( "Case #%d: %d\n", T+1, ans );
    
    }

    return 0;

}