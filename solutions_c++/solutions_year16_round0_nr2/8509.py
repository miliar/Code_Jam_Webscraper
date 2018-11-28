//
//  codejam2.cpp
//  ms_test
//
//  Created by zyy on 16/4/10.
//  Copyright © 2016年 zyy. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int t,n,i,j,l,ii;
char ch,s[10003];

int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.out","w",stdout);
    scanf("%d%ch",&t,&ch);
    for (ii=1; ii<=t; ii++) {
        gets(s);
        l=strlen(s);
        n=0;
        for (i=1; i<l; i++)
            if (s[i]!=s[i-1])
                n++;
        
        if (s[l-1]=='-')
            n++;
        
        printf("Case #%d: %d\n",ii,n);
    }
}