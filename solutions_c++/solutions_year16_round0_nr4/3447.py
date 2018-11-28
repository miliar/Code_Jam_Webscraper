//
//  main.cpp
//  Fractile
//
//  Created by 동교 이 on 2016. 4. 10..
//  Copyright © 2016년 동교 이. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    
    FILE *fp;
    FILE *wfp;
    
    fp = fopen("/Users/Shared/Documents/XCode/2016ACM/Fractile/D-small-attempt0.txt", "r");
    wfp = fopen("/Users/Shared/Documents/XCode/2016ACM/Fractile/output.txt", "w");
    
    int K;
    int C;
    int S;
    
    
    int T = 1;
    
    int num;
    
    fscanf(fp, "%d\n", &num);
    
    while(!feof(fp)) {
        
        fprintf(wfp, "Case #%d:", T);
        fscanf(fp, "%d %d %d\n", &K, &C, &S);
        if(S < K)
            fprintf(wfp, "IMPOSSIBLE\n");
        else {
            for(int i=0; i<K; i++) {
                fprintf(wfp, " %d", i+1);
            }
            fprintf(wfp, "\n");
        }
        T++;
    }
    
    return 0;
}
