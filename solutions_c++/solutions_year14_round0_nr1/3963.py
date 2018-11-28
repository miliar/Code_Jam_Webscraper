//
//  main.cpp
//  codejamProblemA
//
//  Created by Vena Jia Li on 4/11/14.
//  Copyright (c) 2014 Vena Jia Li. All rights reserved.
//


#include <iostream>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>/Users/vena/Documents/vena/codejam/A-small-output.txt
#include <memory.h>
using namespace std;


int main()
{
    int t;
    int first;
    int second;
    int firstboard[4][4];
    int secondboard[4][4];
    int i,j,k;
    bool exist[17];
    freopen("/Users/vena/Documents/vena/codejam/A-small-attempt0.in","r",stdin);
    freopen("/Users/vena/Documents/vena/codejam/A-small-output.txt","w",stdout);
    scanf("%d",&t);
    
    for(i=0;i<t;i++)
    {
        for (j=0;j<17;j++)
        {
            exist[j]=false;
        }
        scanf("%d",&first);
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                scanf("%d",&firstboard[j][k]);
                if(j+1==first)
                {
                    exist[firstboard[j][k]]=true;
                }
            }
        }
        
        scanf("%d",&second);
        int counter=0;
        int result;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                scanf("%d",&secondboard[j][k]);
                if(j+1==second)
                {
                    if(exist[secondboard[j][k]]==true)
                    {
                        counter++;
                        result=secondboard[j][k];
                    }
                }
            }
        }
        
        if(counter==1)
        {
            printf("Case #%d: %d\n",i+1,result);
        }
        else if(counter==0)
        {
            printf("Case #%d: Volunteer cheated!\n",i+1);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",i+1);
        }
    }
    
    
    
    return 0;
}


