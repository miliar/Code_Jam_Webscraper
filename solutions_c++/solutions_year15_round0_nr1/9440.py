//
//  main.cpp
//  CodeJam2015_Q01_A
//
//  Created by Jerry Jiang on 4/11/15.
//  Copyright (c) 2015 Zhilin Jiang. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <fcntl.h>

int main(int argc, const char * argv[]) {
    
    //const char * inFilePath;
    //const char * outFilePath;
    FILE * inFile;
    FILE * outFile;
    
    inFile = fopen("A-large.in", "r");
    outFile = fopen("A.out", "w");
    
    int T;
    fscanf(inFile, "%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        int ans = 0;
        int sum = 0;
        int n;
        fscanf(inFile, "%d", &n);
        char tmpc;
        fscanf(inFile, "%c", &tmpc);
        int tmpd;
        for (int i = 0; i <= n; i++) {
            fscanf(inFile, "%c", &tmpc);
            tmpd = tmpc - '0';
            if (sum < i) {
                ans += (i - sum);
                sum = i + tmpd;
            } else {
                sum += tmpd;
            }
        }
        fprintf(outFile, "Case #%d: %d\n", cases, ans);
        
        
    }
    fclose(inFile);
    fclose(outFile);
    return 0;
}
