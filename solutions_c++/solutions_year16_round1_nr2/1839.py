//
//  main.cpp
//  CodeJam2016
//
//  Created by Young Seok Kim on 4/9/16.
//  Copyright © 2016 TonyKim. All rights reserved.
//

#include <iostream>
#include <string.h>
//#include "bigint.cpp"

using namespace std;


int T;
int N;


int checkmark[2505];


void initialize() {
    for (int i=0; i<2505; i++) {
        checkmark[i] = 0;
    }
}


int main(int argc, const char * argv[]) {
    // insert code here...
    
    freopen("B-large.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d", &T);
    
    int t;
    for (t = 1; t<=T; t++) {
        scanf("%d", &N);
        initialize();
        int num;
        for (int j=1; j<=2*N-1; j++) {
            for (int k=0; k<N; k++) {
                scanf("%d", &num);
                checkmark[num]++;
            }
        }
        printf("Case #%d:", t);
        
        
        // extract odd
        for (int i=0; i<2505; i++) {
            if (checkmark[i] % 2 == 1) {
                printf(" %d", i);
            }
        }
        
        printf("\n");
    }
    
    
    
    
    return 0;
}
