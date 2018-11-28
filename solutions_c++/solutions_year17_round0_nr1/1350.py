//
//  main.cpp
//  test
//
//  Created by 수익 조 on 2017. 1. 5..
//  Copyright © 2016년 수익 조. All rights reserved.
//
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main(void) {
    int testcase = 0;
    freopen("/Users/Sik/Desktop/A-large.in.txt","r",stdin);
    scanf("%d", &testcase);
    
    for(int t = 1; t <= testcase; t++) {
        char s[1111];
        int i,j,len,cnt=0,K;
        scanf("%s%d",&s,&K);
        for(i=0;s[i];++i);
        len=i;
        for(i=0;i<len-K+1;++i)if(s[i]=='-'){++cnt;for(j=0;j<K;++j)s[i+j]=s[i+j]=='-'?'+':'-';}
        for(i=1;i<K;++i)if(s[len-i]=='-')break;
        if(i==K)printf("Case #%d: %d\n",t,cnt);
        else printf("Case #%d: IMPOSSIBLE\n",t);
    }
    
    return 0;
}
