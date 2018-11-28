//
//  main.cpp
//  Google
//
//  Created by Mec0825 on 13-4-13.
//  Copyright (c) 2013年 Mec0825. All rights reserved.
//

#include <iostream>

int main()
{
    freopen("/Users/mec/Documents/Competition/Google/2017/Qualification/A-large.in", "r", stdin);
    freopen("/Users/mec/Documents/Competition/Google/2017/Qualification/A-out.txt", "w", stdout);
    
    int numc;
    
    scanf("%d", &numc);
    
    for(int t = 0; t < numc; t++) {
        
        char S[1001];
        int K;
        
        scanf("%s %d", S, &K);
        
        int res = 0;
        int len = (int)strlen(S);
        for(int i = 0; i <= len-K; i++) {
            if(S[i] == '-') {
                for(int j = 0; j < K; j++) {
                    if(S[i+j] == '+')
                        S[i+j] = '-';
                    else
                        S[i+j] = '+';
                }
                res++;
            }
        }
        
        bool can = true;
        for(int i = len-K; i < len; i++) {
            if(S[i] == '-') can = false;
        }
        
        if(can)
            printf("Case #%d: %d\n",t+1, res);
        else
            printf("Case #%d: IMPOSSIBLE\n",t+1);
        
    }
    
    return 0;
}
