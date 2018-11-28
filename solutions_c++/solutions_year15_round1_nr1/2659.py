//
//  main.cpp
//  CodeJam
//
//  Created by Young Seok Kim on 4/12/15.
//  Copyright (c) 2015 TonyKim. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string.h>


int testcases;

int mushrooms[1005];

int t,b, B,N, cnt, n,i ;



int main(int argc, const char * argv[]) {
    
    freopen("A-large.in-2.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d", &testcases);
    for (t=1; t<=testcases; t++) {
        
        scanf("%d", &N);
        
        for (n=0; n<N; n++) {
            scanf("%d", &mushrooms[n]);
        }
        
        
        // Method 1
        int count1 = 0;
        int maxrate = 0;
        
        for (i=0; i<N-1; i++) {
            if (mushrooms[i]>mushrooms[i+1]) {

                int diff = mushrooms[i]-mushrooms[i+1];
                if (diff>maxrate)
                {
                    maxrate = diff;
                }
                count1 += diff;
            }
        }
        
        // Method 2
        int count2 = 0;
        int minrate = maxrate;
        if (minrate <0) {
            minrate = 0;
        }
        
        for (i=0; i<N-1; i++) {
            if (mushrooms[i]<minrate) {
                count2 += mushrooms[i];
            } else {
                count2 += minrate;
            }
        }
        
        printf("Case #%d: %d %d\n", t, count1, count2);
        
        
    }
    
    
    
    
    
    return 0;
}
