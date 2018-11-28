//
//  main.cpp
//  JamA
//
//  Created by CCH on 2015/4/11.
//  Copyright (c) 2015年 CCH. All rights reserved.
//

#include <iostream>
int main() {
    int T = 0;
    scanf( "%d", &T );
    for (int testCase = 1; testCase <= T ; testCase++) {
        int Smax = 0;
        char ch;
        scanf( "%d%c", &Smax, &ch ); // ch is space
        int SNum[1001], people = 0, ans = 0;
        for ( int run = 0 ; run < Smax+1 ; run++ ) {
            scanf( "%c", &ch );
            SNum[run] = ch - '0';
            if ( run > people && SNum[run] != 0 ) {
                ans += run-people;
                people += run-people;
            } // if
            
            people += SNum[run];
        } // for
        
        printf( "Case #%d: %d\n", testCase, ans );
    } // for
    
    return 0;
}
