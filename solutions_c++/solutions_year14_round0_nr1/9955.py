//
//  main.cpp
//  CODEJAM
//
//  Created by Ashok on 12/04/14.
//  Copyright (c) 2014 Ashok. All rights reserved.
//

#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int cases; cin >> cases;
    int A[4][4],B[4][4];
    for(int i=0;i<cases; i++) {
        int number1; scanf("%d",&number1);
        
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                scanf("%d",&A[j][k]);
            }
        }
        int number2; scanf("%d",&number2);
        
        for(int j=0;j<4;j++) {
            for(int k=0;k<4;k++) {
                scanf("%d",&B[j][k]);
            }
        }
        
        int count =0,ans=0;
        for(int k=0;k<4;k++) {
            for(int j=0;j<4;j++) {
                if(A[number1-1][k]==B[number2-1][j]) {
                    count++;
                    ans = A[number1-1][k];
                }
            }
        }
        if(count==1) {
            printf("Case #%d: %d\n",i+1,ans);
        }
        else if(count==0) {
            printf("Case #%d: Volunteer cheated!\n",i+1);
        }
        else {
            printf("Case #%d: Bad magician!\n",i+1);
        }
    }
}

