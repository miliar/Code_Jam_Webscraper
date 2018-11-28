//
//  main.cpp
//  Round 1B 2014. problem A
//
//  Created by kimtaeyang on 2014. 5. 4..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int N;
char t[102];
int answer;

struct X{
    int n;
    char v[102];
    int c[102];
}a[102];
int abs(int K){return K<0?-K:K;}
int su(int k, int s){
    int i,sum=0;
    for(i=1;i<=N;i++) sum+=abs(a[i].c[k]-s);
    return sum;
}
int min(int x, int y){return x<y?x:y;}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int I,i,j;
    
    int T;
    int s;
    
    scanf("%d",&T);
    
    
    for(I=1;I<=T;I++){
        scanf("%d",&N);
        for(i=1;i<=N;i++) a[i].n=0;
        for(i=1;i<=N;i++){
            scanf("%s",t+1);
            for(j=1;t[j];j++){
                if(t[j]!=t[j-1]){
                    a[i].n++;
                    a[i].v[a[i].n]=t[j];
                    a[i].c[a[i].n]=1;
                }
                else a[i].c[a[i].n]++;
            }
        }
        for(i=1;i<=N;i++) if(a[i].n!=a[1].n) break;
        if(i<N+1) printf("Case #%d: Fegla Won\n",I);
        else {
            for(i=1;i <= a[1].n;i++){
                for(j=1;j<=N;j++) if(a[j].v[i]!=a[1].v[i]) break;
                if(j<N+1) break;
            }
            if(i<a[1].n+1) printf("Case #%d: Fegla Won\n",I);
            else {
                for(i=1;i<=a[1].n;i++){
                    s=0;
                    for(j=1;j<=N;j++) s+=a[j].c[i]; s/=N;
                    answer+=min(su(i,s),su(i,s+1));
                }
                printf("Case #%d: %d\n",I,answer);
                answer=0;
            }
        }
    }
    
    
}