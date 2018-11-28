//
//  main.cpp
//  codejam
//
//  Created by cloudzfy on 6/1/13.
//  Copyright (c) 2013 cloudzfy. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <math.h>
#include <queue>

using namespace std;
int data[120];
int main()
{
    int T,N,M,o,e,p,sum,pp,nsum;
    freopen("A-small-attempt0.in.txt","r",stdin);
	freopen("A-small-attempt0.out.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        sum=0;
        pp=0;
        memset(data,0,sizeof(data));
        scanf("%d%d",&N,&M);
        for(int i=0;i<M;i++)
        {
            scanf("%d%d%d",&o,&e,&p);
            for(int j=o;j<e;j++)
            {
                data[j]+=p;
            }
            sum+=p*(N*2-e+o+1)*(e-o)/2;
            pp+=p;
        }
        nsum=0;
        int flag;
        for(int i=0;i<pp;i++)
        {
            flag=0;
            for(int j=1;j<=N;j++)
            {
                if(data[j]!=0)
                {
                    flag=1;
                    data[j]--;
                    o=j;
                    break;
                }
            }
            if(!flag)
            {
                break;
            }
            for(int j=o+1;j<=N;j++)
            {
                if(data[j]!=0)
                {
                    data[j]--;
                }else {
                    e=j;
                    break;
                }
            }
            nsum+=(N*2-e+o+1)*(e-o)/2;
        }
        printf("Case #%d: %d\n",t,sum-nsum);
    }
    return 0;
}