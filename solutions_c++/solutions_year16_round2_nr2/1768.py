//
//  main.cpp
//  Pro2
//
//  Created by dong on 4/30/16.
//  Copyright © 2016 dong. All rights reserved.
//

#include <iostream>
#include <stdio.h>

#define MAX_LEN 20
#define MAX_VALUE 1000000000000000000

int getlen(char *str) {
    int len = 0;
    while (str[len] != '\0') {++len;}
    return len;
}

FILE *in;
FILE *out;

int n, T;
long long int diff = MAX_VALUE, minS = MAX_VALUE, minJ = MAX_VALUE;
char S[MAX_LEN], J[MAX_LEN], totalS[MAX_LEN], totalJ[MAX_LEN];

void work(int i, int state) {
    if (i < n) {
        if (state == 1) {
            if (S[i] == '?') {
                S[i] = '0';
                if (J[i] == '?') {
                    J[i] = '9';
                    work(i + 1, 1);
                    J[i] = '?';
                } else {
                    work(i + 1, 1);
                }
                S[i] = '?';
            } else {
                if (J[i] == '?') {
                    J[i] = '9';
                    work(i + 1, 1);
                    J[i] = '?';
                } else {
                    work(i + 1, 1);
                }
                
            }
        } else if (state == 2) {
            if (S[i] == '?') {
                S[i] = '9';
                if (J[i] == '?') {
                    J[i] = '0';
                    work(i + 1, 2);
                    J[i] = '?';
                } else {
                    work(i + 1, 2);
                }
                S[i] = '?';
            } else {
                if (J[i] == '?') {
                    J[i] = '0';
                    work(i + 1, 2);
                    J[i] = '?';
                } else {
                    work(i + 1, 2);
                }
                
            }
        } else {
            if (S[i] == '?') {
                if (J[i] == '?') {
                    S[i] = '0';
                    J[i] = '0';
                    work(i + 1, 0);
                    J[i] = '1';
                    work(i + 1, 2);
                    S[i] = '1';
                    J[i] = '0';
                    work(i + 1, 1);
                    J[i] = '1';
                    work(i + 1, 0);
                    S[i] = '?';
                    J[i] = '?';
                } else {
                    if (J[i] > '0') {
                        S[i] = (char)(J[i] - 1);
                        work(i + 1, 2);
                    }
                    S[i] = J[i];
                    work(i + 1, 0);
                    if (J[i] < '9') {
                        S[i] = (char)(J[i] + 1);
                        work(i + 1, 1);
                    }
                    S[i] = '?';
                }
            } else if (J[i] == '?') {
                if (S[i] > '0') {
                    J[i] = (char)(S[i] - 1);
                    work(i + 1, 1);
                }
                J[i] = S[i];
                work(i + 1, 0);
                if (S[i] < '9') {
                    J[i] = (char)(S[i] + 1);
                    work(i + 1, 2);
                }
                J[i] = '?';
            } else {
                if (S[i] < J[i]) {
                    work(i + 1, 2);
                } else if (S[i] > J[i]) {
                    work(i + 1, 1);
                } else {
                    work(i + 1, 0);
                }
            }
        }
    } else {
        //fprintf(out, "S: %s J: %s\n", S, J);
        long long int tmpS;
        long long int tmpJ;
        sscanf(S, "%lld", &tmpS);
        sscanf(J, "%lld", &tmpJ);
        long long tmpdiff = std::abs(tmpS - tmpJ);
        int accept = 0;
        if (tmpdiff < diff) {
            accept = 1;
        } else if (tmpdiff == diff) {
            if (tmpS < minS) {
                accept = 1;
            } else if (tmpS == minS) {
                if (tmpJ < minJ) {
                    accept = 1;
                }
            }
        }
        if (accept == 1) {
            diff = tmpdiff;
            minS = tmpS;
            minJ = tmpJ;
            strcpy(totalS, S);
            strcpy(totalJ, J);
            
        }
        //fprintf(out, "diff: %lld minS: %lld minJ: %lld\n", diff, minS, minJ);
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    in = fopen("B-small-attempt1.in.txt", "r");
    out = fopen("B-small-attempt1.out.txt", "w");
    
    fscanf(in, "%d", &T);fgetc(in);
    for (int k = 1; k <= T; ++k) {
        fscanf(in, "%s", S);
        fscanf(in, "%s", J);
        
        n = getlen(S);
        diff = MAX_VALUE;
        minS = MAX_VALUE;
        minJ = MAX_VALUE;
        
        work(0, 0);
        
        fprintf(out, "Case #%d: %s %s\n", k, totalS, totalJ);
        //fprintf(out, "%lld %lld %lld\n", diff, minS, minJ);
    }
    
    
    fclose(in);
    fclose(out);
    return 0;
}
