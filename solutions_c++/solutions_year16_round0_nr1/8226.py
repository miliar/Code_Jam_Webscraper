//
//  main.cpp
//  TrainingBrain
//
//  Created by David Ko on 1/5/16.
//  Copyright © 2016 David Ko. All rights reserved.
//
//  Subset Sum Problem

#include <stdio.h>

bool digits[10];
int left=10;

void Scatter(int X){
    int a = X;
    while(a > 0){
        if(!digits[a%10]){
            digits[a%10] = true;
            left--;
        }
        a /= 10;
    }
}
void Init(){
    for(int i=0; i<10; i++){
        digits[i] = false;
    }
}
int main(){
    int T = 0, n = 0;
    FILE *in = fopen("A-large.in","r");
    FILE *out = fopen("A-large.out","w");
    fscanf(in, "%d", &T);
    for(int i=1; i<=T; i++){
        fscanf(in, "%d", &n);
        if(n == 0){
            fprintf(out, "Case #%d: INSOMNIA\n", i);
        } else {
            int j = 1;
            Init();
            while(left > 0){
                Scatter(n*j);
                j++;
            }
            fprintf(out, "Case #%d: %d\n", i, n*(j-1));
        }
        left = 10;
    }
    fclose(in);
    fclose(out);
    return 0;
}