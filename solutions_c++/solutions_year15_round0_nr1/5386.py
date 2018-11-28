//
//  main.cpp
//  GCJ2015_A
//
//  Created by 서준호 on 2015. 4. 11..
//  Copyright (c) 2015년 서준호. All rights reserved.
//

#include <stdio.h>
#include <iostream>

int main() {
    int T;
    
    scanf("%d", &T);
    for (int w=0; w<T; w++) {
        int N;
        char in[2000];
        int prev_sum = 0;
        int friends = 0;
        
        scanf("%d %s", &N, in);
        
        for (int i=0; i<=N; i++) {
            prev_sum += (in[i] - '0');
            
            if (prev_sum + friends < i+1) {
                friends = i+1 - prev_sum;
            }
        }
        
        printf("Case #%d: %d\n", w+1, friends);
        
    }
    
    return 0;
}
