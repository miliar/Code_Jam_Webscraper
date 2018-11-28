//
//  main.cpp
//  AlgorithmStudy
//
//  Created by Young Seok Kim on 1/9/14.
//  Copyright (c) 2014 Young Seok Kim. All rights reserved.
//





#include <stdio.h>
#include <string.h>


// Codejam 2014 round1B
// Problem B small.

int testcases; // 1~100






int main(int argc, const char * argv[])
{
    freopen("B-small-attempt0.in.txt","r",stdin);
    //freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    
    scanf("%d", &testcases);
    for (int i=1; i<=testcases; i++) {
        
        int A,B,K;
        scanf("%d %d %d", &A, &B, &K);
        int count=0;
        for (int x=0; x<A; x++) {
            for (int y=0; y<B; y++) {
                if ((x&y) < K) {
                    //printf("A,B,A&B is : %d %d %d\n", A, B, A&B);
                    count++;
                }
            }
        }
        printf("Case #%d: %d\n",i, count);
        
    }
    
}