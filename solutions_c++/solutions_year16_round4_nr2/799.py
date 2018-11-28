//
//  main.cpp
//  red_tape_commitee
//
//  Created by Matjaz Leonardis on 28/05/2016.
//  Copyright © 2016 Matjaz Leonardis. All rights reserved.
//

#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;


int T;

long double p[500];
int N,K;


long double pmax[205][205][205];


long double f(int n,int k,int target){
    
    printf("%d %d %d\n",n,k,target);
    
    if (target > n + 1) return 0;
    if (k > n + 1) return 0;
    if (target > k) return 0;
    if (target < 0) return 0;
    
    if (k == 0){
        if (target == 0) return 1.0;
        return 0.0;
    }
    
    pmax[n][k][target] = max(f(n-1,k,target), p[n] * f(n-1,k-1,target - 1) + (1-p[n]) * f(n-1,k-1,target));
    
    printf("%d %d %d %Lf\n",n,k,target,pmax[n][k][target]);
    
    return pmax[n][k][target];

}

int main(int argc, const char * argv[]) {
    
    scanf("%d",&T);
    
    for (int caseNumber = 1;caseNumber <=T; caseNumber ++){
        scanf("%d %d",&N,&K);
        for (int i=0;i<N;i++) scanf("%Lf",&p[i]);
        
        long double bestProb = 0.0;
        
        for (int i=0;i<(1<<N);i++){
            if (__builtin_popcount(i) != K) continue;
            long double prob[20];
            memset(prob,0,sizeof prob);
            prob[0] = 1.0;
            for (int j=0;j<N;j++){
                if ((i & (1<<j)) == 0) continue;
                long double newProb[20];
                memset(newProb, 0, sizeof(newProb));
                for (int k=0;k<=K;k++) {
                    if (k== 0) newProb[k] = (1- p[j]) * prob[0]; else newProb[k] = p[j] * prob[k-1] + (1-p[j]) * prob[k];
                }
                for (int k=0;k<K;k++) prob[k] = newProb[k];
            }
            
            if (prob[K/2] > bestProb) bestProb = prob[K/2];
        }
        
        printf("Case #%d: %.8Lf\n",caseNumber,bestProb);
        
    }
    
    
    return 0;
}
