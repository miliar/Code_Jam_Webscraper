//
//  main.cpp
//  CodeJam2016
//
//  Created by Young Seok Kim on 4/9/16.
//  Copyright © 2016 TonyKim. All rights reserved.
//

#include <iostream>



int T;


bool digitsAppear[10];


void initialize() {
    for (int i=0; i<10; i++) {
        digitsAppear[i] = false;
    }
}

bool checkSleep() {
    for (int i=0; i<10; i++) {
        if (digitsAppear[i] == false) {
            return false;
        }
    }
    return true;
}


void digitCheck(long long int k ) {
    while (k!=0) {
        int digit = k % 10;
        digitsAppear[digit] = true;
        k/=10;
    }
}


int main(int argc, const char * argv[]) {
    // insert code here...
    
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int N;
        scanf("%d", &N);
        initialize();
        
        long long int multiples = N;
        printf("Case #%d: ", t);
        if (N==0) {
            printf("INSOMNIA\n");
        } else {
            digitCheck(multiples);
            while (!checkSleep()) {
                // digitsAppear
                multiples += N;
                digitCheck(multiples);
            }
            printf("%lld\n", multiples);
        }
    }

    return 0;
}
