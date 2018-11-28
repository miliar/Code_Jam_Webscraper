//
//  P1.cpp
//  CodeJamTest
//
//  Created by Manh Tung Pham on 4/12/15.
//  Copyright (c) 2015 Manh Tung Pham. All rights reserved.
//

#include <stdio.h>
#include <iostream>

using namespace std;

int Solve(int* val, int n);

int main(){
    freopen ("A-large.in.txt", "r", stdin);
    freopen ("A-large.out.txt","w",stdout);
    
    int T;
    scanf("%d\n", &T);
    for(int nprob = 1; nprob <= T; ++nprob) {
        int Smax;
        scanf("%d", &Smax);
        
        char S[Smax + 1];
        int val[Smax + 1];
        scanf("%s\n", S);
        
        for(int i = 0; i <= Smax; ++i){
            val[i] = S[i] - '0';
        }
        int x = Solve(val, Smax + 1);
        
        printf("Case #%d: %d\n", nprob, x);
    }
    fclose(stdin);
    fclose (stdout);
    return 0;
}

int Solve(int* S, int n){
    int res = 0;
    int dp = S[0];
    for(int i = 1; i < n; ++i){
        if(S[i] > 0 && (dp + res < i)){
            res += (i - dp - res);
        }
        dp += S[i];
    }
    return res;
}