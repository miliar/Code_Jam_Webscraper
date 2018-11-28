//
//  main.cpp
//  codejam
//
//  Created by shawpan on 4/12/14.
//  Copyright (c) 2014 shawpan. All rights reserved.
//
#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;

int main(int argc, const char * argv[])
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,n,k,j,d,w;
    long double na[1500],ken[1500];
    
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
        for(j=0;j<n;++j)
        {
            scanf("%Lf",&na[j]);
        }
        
        for(j=0;j<n;++j)
        {
            scanf("%Lf",&ken[j]);
        }
        
        sort(na,na+n);
        sort(ken, ken+n);
        
        j=k=0;
        while(j<n && k<n)
        {
            if(na[j] >= ken[k])
            {
                j++;k++;
            }
            else
            {
                j++;
            }
        }
        d = k;
        j=k=n-1;w=0;
        while(j>=0 && k>=0)
        {
            if(na[j] > ken[k])
            {
                j--;w++;
            }
            else
            {
                j--;k--;
            }
        }
        printf("Case #%d: %d %d\n",i,d,w);
    }
    return 0;
}

