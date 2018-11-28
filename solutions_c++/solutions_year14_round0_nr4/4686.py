//
//  main.cpp
//  AlgorithmStudy
//
//  Created by Young Seok Kim on 1/9/14.
//  Copyright (c) 2014 Young Seok Kim. All rights reserved.
//



#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;


// Problem D. Deceitful War

int T; // 1~50
double naomi[1005];
double ken[1005];
bool naomi_used[1005];
bool ken_used[1005];

int answer_optimal[60];
int answer_normal[60];


int main(int argc, const char * argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d", &T);
    
    for (int t=0; t<T; t++) {
        int N; // 1~1000
        scanf("%d", &N);
        for (int i=0; i<N; i++) {
            scanf("%lf", &naomi[i]);
        }
        for (int i=0; i<N; i++) {
            scanf("%lf", &ken[i]);
        }

        sort(naomi,naomi+N);  // - Ascending order
        sort(ken,ken+N); // - Ascending order
        
        
        
        
        // Optimal calculation
        
        for (int k=0; k<N; k++) {
            ken_used[k]=0;
            naomi_used[k]=0;
        }
        
        
        

        for (int k=N-1; k>=0; k--) {
            if (ken[k]<naomi[N-1]) {
                break;
            }
            ken_used[k]=true;
            naomi_used[N-1-k]=true;
        }
        int win=0;
        for (int k=0; k<N; k++) {
            if (!ken_used[k]) {
                for (int j=0; j<N; j++) {
                    if (!naomi_used[j]) {
                        if (naomi[j] >ken[k]) {
                            ken_used[k]=true;
                            naomi_used[j]=true;
                            win++;
                            break;
                        }
                    }
                }
            }
        }
        
        answer_optimal[t] = win;
        
        
        // Normal calculation
        
        for (int k=0; k<N; k++) {
            ken_used[k]=0;
        }
        
        
        
        int losecount = 0;
        for (int k=0; k<N; k++) {
            double naomi_chosen = naomi[k];
            for (int j=0; j<N; j++) {
                if (!ken_used[j]) {
                    if (naomi_chosen < ken[j]) {
                        ken_used[j]=true;
                        losecount++;
                        break;
                    }
                }
                
            }
        }
        answer_normal[t] = N - losecount;
    }
    for (int i=0; i<T; i++) {
        printf("Case #%d: %d %d\n", i+1, answer_optimal[i], answer_normal[i]);
    }
    
   
    
}











