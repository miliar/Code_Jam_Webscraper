//
//  main.cpp
//  GCJ2014
//
//  Created by 宋 良骏 on 4/12/14.
//  Copyright (c) 2014 宋 良骏. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main()
{
   	freopen("1.in","r",stdin);
    freopen("1res.txt","w",stdout);
    int Case;
    scanf("%d",&Case);
    int before, after;
    int bmt[4][4];
    int amt[4][4];
    for(int c= 1;c<=Case;c++)
    {
        scanf("%d",&before);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&bmt[i][j]);
            }
        }
        scanf("%d",&after);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&amt[i][j]);
            }
        }
        int ct=0, res = -1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(bmt[before - 1][i] == amt[after - 1][j])
                {
                    ct++;
                    res = bmt[before - 1][i];
                }
            }
        }
        printf("Case #%d: ",c);
        if(ct==0)
            printf("Volunteer cheated!\n");
        if(ct == 1)
            printf("%d\n",res);
        if(ct> 1)
            printf("Bad magician!\n");
    }
    
    
    
    return 0;
}

