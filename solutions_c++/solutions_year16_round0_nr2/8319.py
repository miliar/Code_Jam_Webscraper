//
//  main.cpp
//  TrainingBrain
//
//  Created by David Ko on 1/5/16.
//  Copyright © 2016 David Ko. All rights reserved.
//
//  Subset Sum Problem

#include <stdio.h>
#include <string.h>

int main(){
    FILE *in = fopen("B-large.in", "r");
    FILE *out = fopen("B-large.out", "w");
    int T, len, cnt=0;
    char input[100];
    fscanf(in, "%d", &T);
    for(int t=1; t<=T; t++){
        fscanf(in, "%s", input);
        len = (unsigned)strlen(input);
        for(int i=1; i<len; i++){
            if(input[i] != input[i-1]) cnt++;
        }
        if(input[len-1] == '-') cnt++;
        fprintf(out, "Case #%d: %d\n", t, cnt);
        cnt = 0;
    }
    fclose(in);
    fclose(out);
    return 0;
}