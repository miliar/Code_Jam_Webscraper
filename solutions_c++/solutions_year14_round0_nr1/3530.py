//
//  main.cpp
//  CodeJam A
//
//  Created by Baker Mohd Anas on 4/12/14.
//  Copyright (c) 2014 Baker Mohd Anas. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[])
{
    freopen("/Users/Baker/Desktop/CodeJam_A/test.in", "r", stdin);
    freopen("/Users/Baker/Desktop/CodeJam_A/A.out", "w", stdout);
    // insert code here...
    
    int Case = 1,test,ans1,ans2,grid1[4][4],grid2[4][4],ans = -1, total_match;
    
    scanf("%d",&test);
    
    
    while(test--)
    {
        scanf("%d",&ans1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&grid1[i][j]);
        
        scanf("%d",&ans2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&grid2[i][j]);
        
        total_match = 0;
        ans1--; ans2--;
        for(int i=0;i<4;i++)
        {
            int val = grid1[ans1][i];
            //printf("val:%d\n",val);
            for(int j=0;j<4;j++)
                if(val == grid2[ans2][j])
                {
                    total_match++;
                    ans = val;
                }
        }
        //printf("Total Match: %d\n", total_match);
        printf("Case #%d: ", Case++);
        if(total_match == 0)
            printf("Volunteer cheated!\n");
        else if(total_match>1)
            printf("Bad magician!\n");
        else printf("%d\n",ans);
    }
    
    return 0;
}

