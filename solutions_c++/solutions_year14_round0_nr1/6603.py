//
//  main.cpp
//  Magic Trick
//
//  Created by Estelle :) on 12/4/14.
//  Copyright (c) 2014 AWESOMENESS. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
    freopen("/Users/student/Downloads/A-small-attempt2.in", "r", stdin);
    int T;
    scanf("%d", &T);
    int ans[T];
    for (int i=0; i<T; i++)
    {
        int r1, pos1[4];
        scanf("%d", &r1);
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            {
                int a;
                scanf("%d", &a);
                if (j==r1-1)
                {
                    pos1[k]=a;
                }
            }
        }
        int r2;
        int b;
        bool exist=false;
        bool exist2=false;
        scanf("%d", &r2);
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            {
                int a;
                scanf("%d", &a);
                if (j==r2-1)
                {
                    for (int l=0; l<4; l++)
                    {
                        if (a==pos1[l])
                        {
                            if (exist)
                            {
                                exist2=true;
                            }
                            exist=true;
                            b=a;
                        }
                    }
                }
            }
        }
        if (exist && !exist2)
        {
            ans[i]=b;
        }
        else if (exist && exist2)
        {
            ans[i]=-1;
        }
        else {
            ans[i]=0;
        }
    }
    for (int i=0; i<T; i++)
    {
        if (ans[i]==0)
        {
            printf("Case #%d: Volunteer cheated!\n", i+1);
        }
        else if (ans[i]==-1)
        {
            printf("Case #%d: Bad magician!\n", i+1);
        }
        else {
            printf("Case #%d: %d\n", i+1, ans[i]);
        }
    }
}

