//
//  main.cpp
//  codejam
//
//  Created by Apple on 16/4/9.
//  Copyright © 2016年 Apple. All rights reserved.
//

#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define maxn 10005
char s[maxn];
int main()
{
    
    freopen("/Users/apple/Desktop/in.txt","r",stdin);
    freopen("/Users/apple/Desktop/out.txt","w",stdout);
    int t;
    int cas=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        int num=1;
        int l=strlen(s);
        for(int i=1;s[i];i++){
            if(s[i]!=s[i-1]) num++;
        }
        
        if(s[l-1]=='+'){
            num--;
        }
        
        printf("Case #%d: %d\n",cas++,num);
        
    }
}