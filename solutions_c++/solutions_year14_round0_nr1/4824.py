//
//  main.cpp
//  AlgorithmStudy
//
//  Created by Young Seok Kim on 1/9/14.
//  Copyright (c) 2014 Young Seok Kim. All rights reserved.
//



#include <stdio.h>
#include <string.h>

// Problem A. Magic Trick

int T; // 1~100
int first_arrangement[4][4]; // 0~3, 0~3
int second_arrangement[4][4];
int probability[20]; // 1~16

int main(int argc, const char * argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d",&T);
    
    for (int t=0; t<T; t++) {
        
        for (int k=0; k<20; k++) {
            probability[k]=0;
        }
        
        
        int first_answer;
        scanf("%d", &first_answer); // 1~4
        for (int i=0; i<4; i++) {
            scanf("%d %d %d %d", &first_arrangement[i][0], &first_arrangement[i][1], &first_arrangement[i][2], &first_arrangement[i][3]);
            if (first_answer-1 == i) {
                probability[first_arrangement[i][0]]+=1;
                probability[first_arrangement[i][1]]+=1;
                probability[first_arrangement[i][2]]+=1;
                probability[first_arrangement[i][3]]+=1;
            }
        }
        
        int second_answer;
        scanf("%d", &second_answer);
        for (int i=0; i<4; i++) {
            scanf("%d %d %d %d", &second_arrangement[i][0], &second_arrangement[i][1], &second_arrangement[i][2], &second_arrangement[i][3]);
            if (second_answer-1 == i) {
                probability[second_arrangement[i][0]]+=1;
                probability[second_arrangement[i][1]]+=1;
                probability[second_arrangement[i][2]]+=1;
                probability[second_arrangement[i][3]]+=1;
            }
            
        }
        
        int answer=0;
        int no_of_answers=0;
        for (int j=1; j<17; j++) {
            if (probability[j]==2) {
                no_of_answers+=1;
                answer=j;
            }
            
        }
        
        
        if (no_of_answers==0) {
            printf("Case #%d: Volunteer cheated!\n",t+1);
        }
        else if (no_of_answers==1) {
            printf("Case #%d: %d\n", t+1, answer);
        }
        else {
            printf("Case #%d: Bad magician!\n",t+1);
        }
        
        
    }
    
    
    
}











