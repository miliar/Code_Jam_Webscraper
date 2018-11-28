//
//  main.cpp
//  Codejam
//
//  Created by Sorawit Suriyakarn on 4/13/13.
//  Copyright (c) 2013 Sorawit Suriyakarn. All rights reserved.
//

#include <iostream>
#include <cstdio>

int t;
int n,m;
int A[210][210];

bool prog()
{
    scanf("%d%d",&n,&m);
    for(int c=1;c<=n;c++) for(int d=1;d<=m;d++) scanf("%d",&A[c][d]);
    for(int c=1;c<=n;c++) for(int d=1;d<=m;d++)
    {
        for(int e=1;e<=n;e++) if( A[e][d] > A[c][d] ) goto P1;
        continue;
        P1:;
        for(int e=1;e<=m;e++) if( A[c][e] > A[c][d] ) goto P2;
        continue;
        P2:;
        return false;
    }
    return true;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/thepsint/Desktop/in.txt","r",stdin);
    freopen("/Users/thepsint/Desktop/out.txt","w",stdout);
    //printf("gg\n");
    scanf("%d",&t);
    for(int c=1;c<=t;c++)
    {
        printf("Case #%d: ",c);
        if( prog() ) printf("YES\n");
        else printf("NO\n");
    }

    return 0;
}

