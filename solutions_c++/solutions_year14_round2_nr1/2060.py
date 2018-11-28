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
// Problem A.

int testcases; // 1~100
bool impossible;
int N;
char strings[110][110]; // wordindex, letters
char concatenation[110][110]; // wordindex, letters
int lettercount[110][110]; // wordindex, each concatenated letters
int avg[110];  // for each concatenated letters



int absolute(int n)
{
    if (n>=0) {
        return n;
    }
    else {
        return -n;
    }
    
}




int main(int argc, const char * argv[])
{
    freopen("A-small-attempt0.in.txt","r",stdin);
    //freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    
    scanf("%d", &testcases);
    for (int i=1; i<=testcases; i++) {
        impossible=false;
        int moves = 0;
        for (int b = 0; b<110; b++) {
            for (int c = 0; c<110; c++) {
                //strings[b][c]=0;
                concatenation[b][c]=0;
                lettercount[b][c]=0;
                avg[c]=0;
            }
        }
        
        
        // end of reset initialization
        
        
        
        
        scanf("%d",&N);
        for (int k=0; k<N; k++) {
            scanf("%s", strings[k]);
        }
        
        for (int k=0; k<N; k++) {
            char compare = strings[k][0];
            concatenation[k][0] = compare;
            int index = 1;
            for (int h=1; h<strlen(strings[k]); h++) {
                if (compare == strings[k][h]) {
                    continue;
                }
                else {
                    concatenation[k][index]=strings[k][h];
                    compare = strings[k][h];
                    index++;
                }
            }
        }
        
        for (int k=0; k<N; k++) {
            if (strcmp(concatenation[k],concatenation[0]) != 0 ){
                impossible=true;
            }
        }
        
        if (!impossible) {
            for (int k=0; k<N; k++) {
                int index=0;
                for (int a=0; a<strlen(concatenation[0]); a++) {
                    while (concatenation[0][a] == strings[k][index]) {
                        lettercount[k][a]++;
                        index++;
                    }
                    index++;
                }
            }
        }
        for (int a=0; a<strlen(concatenation[0]); a++) {
            int summation = 0;
            for (int k=0 ; k<N; k++) {
                summation += lettercount[k][a];
            }
            int average_floor = summation/N;
            float average = summation/N;
            if (average - average_floor >= 0.5) {
                average_floor += 1;
            }
            avg[a] = average_floor;
        }
        
        
        for (int a=0; a<strlen(concatenation[0]); a++) {
            for (int k=0; k<N; k++) {
                moves += absolute(lettercount[k][a] - avg[a]);
            }
        }
        
        
        
        
        
        
        
        
        if (impossible) {
            printf("Case #%d: Fegla Won\n",i);
        }
        else {
            printf("Case #%d: %d\n",i, moves);
        }
    }
    
}