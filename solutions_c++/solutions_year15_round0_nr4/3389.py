//
//  main.cpp
//  CodeJam
//
//  Created by Young Seok Kim on 4/12/15.
//  Copyright (c) 2015 TonyKim. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string.h>


int testcases;

bool alwaysPossible[25][25][25];


int main(int argc, const char * argv[]) {
    
    freopen("D-small-attempt1.in-2.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int t;
    
    
    alwaysPossible[1][1][1]=true;
    
    alwaysPossible[1][1][2]=true;
    alwaysPossible[2][1][2]=true;
    
    alwaysPossible[1][1][3]=true;
    
    alwaysPossible[1][1][4]=true;
    alwaysPossible[2][1][4]=true;
    
    
    alwaysPossible[1][2][1]=true;
    alwaysPossible[2][2][1]=true;
    
    alwaysPossible[1][2][2]=true;
    alwaysPossible[2][2][2]=true;
    
    alwaysPossible[1][2][3]=true;
    alwaysPossible[2][2][3]=true;
    alwaysPossible[3][2][3]=true;
    
    alwaysPossible[1][2][4]=true;
    alwaysPossible[2][2][4]=true;
    
    alwaysPossible[1][3][1]=true;
    
    alwaysPossible[1][3][2]=true;
    alwaysPossible[2][3][2]=true;
    alwaysPossible[3][3][2]=true;
    
    alwaysPossible[1][3][3]=true;
    alwaysPossible[3][3][3]=true;
    
    alwaysPossible[1][3][4]=true;
    alwaysPossible[2][3][4]=true;
    alwaysPossible[3][3][4]=true;
    alwaysPossible[4][3][4]=true;
    
    alwaysPossible[1][4][1]=true;
    alwaysPossible[2][4][1]=true;
    
    alwaysPossible[1][4][2]=true;
    alwaysPossible[2][4][2]=true;
    
    alwaysPossible[1][4][3]=true;
    alwaysPossible[2][4][3]=true;
    alwaysPossible[3][4][3]=true;
    alwaysPossible[4][4][3]=true;
    
    alwaysPossible[1][4][4]=true;
    alwaysPossible[2][4][4]=true;
    alwaysPossible[4][4][4]=true;
    
    
    
    
    
    scanf("%d", &testcases);
    for (t=1; t<=testcases; t++) {
        int x,r,c;
        scanf("%d %d %d", &x, &r, &c);
        
        if ((r*c)%x != 0) {
            printf("Case #%d: RICHARD\n", t);
        } else {
            if (alwaysPossible[x][r][c]) {
                printf("Case #%d: GABRIEL\n", t);
            } else {
                printf("Case #%d: RICHARD\n", t);
            }
        }
        
    }
    
    
    
    
    
    return 0;
}
