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
#include <string>
using namespace std;

int t,n,i,j,k,l,ii,ok,yes;
char ch,s[10003];
int cnt[10][26]={0};
int ans[2000],len;
int cur[26];
string number[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};

void dfs(int depth, int start) {
    int i,j,fin,ok;
    
    fin=1;
    for (i=0; i<26; i++)
        if (cur[i]!=0)
            fin=0;
    
    if (fin==1) {
        yes=1;
        len=depth;
        return;
    }
    
    for (i=start; i<=9; i++) {
        ok=1;
        for (j=0; j<26; j++)
            if (cur[j]<cnt[i][j])
                ok=0;
        
        if (ok==1) {
            ans[depth]=i;
            for (j=0; j<26; j++)
                cur[j]-=cnt[i][j];
            
            dfs(depth+1,i);
            if (yes==1)
                return;
            
            for (j=0; j<26; j++)
                cur[j]+=cnt[i][j];
        }
    }
}

int main()
{
    freopen("input11.in","r",stdin);
    freopen("output11.out","w",stdout);
    for (i=0; i<=9; i++) {
        for (j=0; j<number[i].length(); j++)
            cnt[i][number[i][j]-'A']++;
    }
    
    scanf("%d%ch",&t,&ch);
    for (ii=1; ii<=t; ii++) {
        gets(s);
        l=strlen(s);
        for (i=0; i<l; i++)
            cur[s[i]-'A']++;
        
        yes=0;
        dfs(0,0);
        printf("Case #%d: ",ii);
        for (i=0; i<len; i++) {
            printf("%d",ans[i]);
        }
        
        printf("\n");
    }
}