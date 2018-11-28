//
//  main.cpp
//  magicTrick
//
//  Created by Jacob on 12/04/14.
//  Copyright (c) 2014 Jacob. All rights reserved.
//

#include <cstdio>

int main(int argc, const char * argv[])
{
    int testCases;
    scanf("%d", &testCases);
    
    for (int i=1; i<=testCases; i++) {
        int table[4][4];
        int ans1, ans2;
        
        scanf("%d", &ans1);
        for (int j=0; j<4; j++) {
            scanf("%d %d %d %d", &table[j][0], &table[j][1], &table[j][2], &table[j][3]);
        }
        scanf("%d", &ans2);
        
        int candidates[4];
        candidates[0] = table[ans1-1][0];
        candidates[1] = table[ans1-1][1];
        candidates[2] = table[ans1-1][2];
        candidates[3] = table[ans1-1][3];
        
        for (int j=0; j<4; j++) {
            scanf("%d %d %d %d", &table[j][0], &table[j][1], &table[j][2], &table[j][3]);
        }
        
        int ans = 0;
        bool cheated = false;
        for (int j=0; j<4; j++) {
            for(int k=0; k<4; k++) {
                if (candidates[j] == table[ans2-1][k]) {
                    if (ans) {
                        cheated = true;
                    }
                    ans = candidates[j];
                }
            }
        }
        
        if (cheated) {
            printf("Case #%d: Bad magician!\n", i);
        }
        
        else if (ans != 0) {
            printf("Case #%d: %d\n", i, ans);
        }
        
        else printf("Case #%d: Volunteer cheated!\n", i);
    }
    
    return 0;
}

