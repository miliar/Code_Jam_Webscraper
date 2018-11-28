//
//  main.cpp
//  StandingOvation
//
//  Created by 용일 장 on 2015. 4. 11..
//  Copyright (c) 2015년 용일 장. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>

/*
 Input
 
 4
 4 11111
 1 09
 5 110011
 0 1
 
 Output

 Case #1: 0
 Case #2: 1
 Case #3: 2
 Case #4: 0
*/

int main2(int smax, char* s) {
    int need = 0;
    int curSum = 0;
    for( int i = 0 ; i < smax ; i++) {
        int cur = (int)(s[i] - '0');
        curSum += cur;
        if (curSum < (i + 1)) {
            need += (i + 1) - curSum;
            curSum = i + 1;
        }
    }
    return need;
}

int main(int argc, const char * argv[]) {
    int T;
    int max;
    char s[1001];
    FILE* fp = fopen("input.txt", "r");
    if(fp == NULL) {
        fprintf(stderr, "file open error\n");
        return -1;
    }
    fscanf(fp, "%d", &T);
    
    for(int i = 0 ; i < T ; i++) {
        fscanf(fp, "%d", &max);
        fscanf(fp, "%s", s);
        int ret = main2(max, s);
        printf("Case #%d: %d\n", i + 1, ret);
    }
    return 0;
}
