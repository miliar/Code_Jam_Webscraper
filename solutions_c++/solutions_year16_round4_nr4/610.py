//
//  main.cpp
//  freeform_factory
//
//  Created by Matjaz Leonardis on 28/05/2016.
//  Copyright © 2016 Matjaz Leonardis. All rights reserved.
//

#include <stdio.h>
#include <algorithm>

using namespace std;

int T;

int canOperate[10][10];

int N;

int p[5];
int tmp[5][5];
int taken[5];

char raw[10][10];



bool canDo(int x){
    //printf("%d\n",x);
    if (x==N) return true;
    bool canAssign = false;
    for (int i=0;i<N;i++) if (tmp[p[x]][i] && taken[i] == 0){
        canAssign = true;
        taken[i] = 1;
        if (!canDo(x+1)) return false;
        taken[i] = 0;
    }
    return canAssign;
}



bool works(int bitmask){
    
    //if (bitmask == 15) printf("HEY");
    
    for (int i=0;i<N;i++)
        for (int j=0;j<N;j++) if ((bitmask & (1<<(N*i + j))) != 0) tmp[i][j] = 1; else tmp[i][j] = 0;
    
    for (int i=0;i<N;i++) p[i] = i;
    
    do{
        //if (bitmask == 15) printf("BLA\n");
        for (int i=0;i<N;i++) taken[i] = 0;
        if (!canDo(0)) return false;
    } while (next_permutation(p, p+N));
    
    return true;
    
}

int main() {
    
    scanf("%d",&T);
    
    for (int caseNumber = 1;caseNumber <= T; caseNumber++){
        
        scanf("%d",&N);
        
        for (int i=0;i<N;i++) scanf("%s",raw[i]);
        
        for (int i=0;i<N;i++)
            for (int j=0;j<N;j++) if (raw[i][j]=='1') canOperate[i][j] = 1; else canOperate[i][j] = 0;
            
        
        int bitmask = 0;
        
        for (int i=0;i<N;i++)
            for (int j=0;j<N;j++) bitmask += canOperate[i][j] * (1<<(N*i + j));
        
        
        int best = N * N + 1;
        
        for (int i=0;i< (1<<(N*N));i++){
            
            int payment = __builtin_popcount(i);
            
            if (payment < best){
                if (works(i | bitmask)) best = payment;
            }
        }
        
        printf("Case #%d: %d\n",caseNumber,best);
        fprintf(stderr,"Done case %d.\n", caseNumber);
        
        
    }
    

    return 0;
}
