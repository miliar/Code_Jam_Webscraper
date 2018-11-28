//
//  main.cpp
//  Round 1C 2014. Problem B. Reordering Train Cars
//
//  Created by kimtaeyang on 2014. 5. 11..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int n;
char a[102][105];
int len[102];
int v[102];
int ch[500];
int count;
int ans[100];

void f(char last ,int pre){
    if(pre==n){
        count++;
        return ;
    }
    if(!pre){
        int i,j;
        for(i=1;i<=n;i++){
            a[i][0]=0;
            for(j=1;j<=len[i];j++){
                if(a[i][j]!=a[i][j-1]){
                    if(ch[a[i][j]]) break;
                    else ch[a[i][j]]=1;
                }
            }
            v[i]=1;
            ans[pre]=i;
            if(j==len[i]+1) f(a[i][len[i]],pre+1);
            v[i]=0;
            for(j='a';j<='z';j++) ch[j]=0;
        }
        return ;
    }
    int i,j;
    int st[100],N=0;
    for(i=1;i<=n;i++)if(!v[i]){
        a[i][0]=last;
        for(j=1;j<=len[i];j++){
            if(a[i][j]!=a[i][j-1]){
                if(ch[a[i][j]]) break;
                else ch[a[i][j]]=1, st[N++]=a[i][j];
            }
        }
        v[i]=1;
        ans[pre]=i;
        if(j==len[i]+1) f(a[i][len[i]],pre+1);
        v[i]=0;
        for(j=0;j<N;j++) ch[st[j]]=0;
        N=0;
    }
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T,I;
    int i;
    
    scanf("%d",&T);
    for(I=1;I<=T;I++){
        scanf("%d",&n);
        for(i=0;i<500;i++) ch[i]=0;
        for(i=1;i<=n;i++) scanf("%s ",a[i]+1), len[i]=strlen(a[i]+1);

        count=0;
        f(0,0);
        
        printf("Case #%d: %d\n",I,count);
    }
}