//
//  main.cpp
//  MagicTrick
//
//  Created by 向仁楷 on 14-4-12.
//  Copyright (c) 2014年 Giraffe-Tech. All rights reserved.
//

#include <iostream>
#include <stdio.h>

int m1[4][4],m2[4][4];

int main(int argc, const char * argv[])
{
    int i,j,k,tc,r1,r2,cnt,ans;
    
    freopen("./A-small-attempt1.in", "r", stdin);
    freopen("./A-small-attempt1.out", "w", stdout);
    
    scanf("%d",&tc);
    for (k = 1; k <= tc; k ++) {
        
        cnt = 0;
        ans = 0;
        scanf("%d",&r1);
        r1 --;
        for (i = 0; i < 4; i ++) {
            for (j = 0; j < 4; j ++) {
                scanf("%d",&m1[i][j]);
            }
        }
        
        scanf("%d",&r2);
        r2 --;
        for (i = 0; i < 4; i ++) {
            for (j = 0; j < 4; j ++) {
                scanf("%d",&m2[i][j]);
            }
        }
        
        for (i = 0; i < 4; i ++) {
            for (j = 0; j < 4; j ++) {
                if (m1[r1][i] == m2[r2][j]) {
                    cnt ++;
                    ans = m1[r1][i];
                }
            }
        }
        
        if (cnt == 0) {
            printf("Case #%d: Volunteer cheated!\n",k);
        }
        if (cnt == 1) {
            printf("Case #%d: %d\n",k,ans);
        }
        if (cnt > 1) {
            printf("Case #%d: Bad magician!\n",k);
        }

    }
    

    return 0;
}

