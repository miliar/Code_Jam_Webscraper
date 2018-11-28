//
//  main.cpp
//  Round 1B 2014. problem C
//
//  Created by kimtaeyang on 2014. 5. 4..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>
#include <algorithm>

int trans[60];

int n,m;
int v[60][60];
int check[60];
int answer[60], path[60];

struct X{
    int num, zip, rank;
    bool operator()(X aa, X bb){
        return aa.zip<bb.zip;
    }
}a[60];
struct Y{
    bool operator()(X aa, X bb){
        return aa.num<bb.num;
    }
};

void f(int x, int t, int c){
    //printf("(%d %d %d)\n",x,t,c);
    //for(int i=1;i<=n;i++) printf("%d ",answer[i]); printf("\n");
    //for(int i=1;i<=t;i++) printf("%d ",path[i]); printf("\n\n");
    int i;
    if(t==n){
        for(i=1;i<=n;i++) if(answer[i]!=path[i]) break;
        if(answer[i]<path[i] && answer[1]) return;
        for(i=1;i<=n;i++) answer[i]=path[i];
        return ;
    }
    check[x]++;
    for(i=1;i<=n;i++){
        if(!check[i] && v[x][i]){
            v[x][i]=0, path[t+1]=i, f(i,t+1,0), v[x][i]=1;
            /*if(!answer[t+1] || !c) v[x][i]=0, path[t+1]=i, f(i,t+1,0), v[x][i]=1;
            else if(answer[t+1]==i) v[x][i]=0, path[t+1]=i, f(i,t+1,1), v[x][i]=1;
            else if(answer[t+1]>i) v[x][i]=0, path[t+1]=i, f(i,t+1,0),v[x][i]=1;*/
        }
        else if(v[x][i] && !v[i][x]){
            v[x][i]=0; f(i,t,c); v[x][i]=1;
            /*if(!answer[t+1] || !c) v[x][i]=0, path[t+1]=i, f(i,t+1,0), v[x][i]=1;
            else if(answer[t+1]==i) v[x][i]=0, path[t+1]=i, f(i,t+1,1), v[x][i]=1;
            else if(answer[t+1]>i) v[x][i]=0, path[t+1]=i, f(i,t+1,0),v[x][i]=1;*/
        }
    }
    check[x]--;
}


int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int I,i,j,k;
    
    int T;
    
    scanf("%d",&T);
    
    for(I=1;I<=T;I++){
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++) for(j=1;j<=n;j++) v[i][j]=0;
        for(i=1;i<=n;i++) scanf("%d",&a[i].zip), a[i].num=i;
        std::sort(a+1,a+1+n,X());
        for(i=1;i<=n;i++) a[i].rank=i;
        std::sort(a+1,a+1+n,Y());
        for(i=1;i<=m;i++){
            scanf("%d%d",&j,&k);
            v[a[j].rank][a[k].rank] = v[a[k].rank][a[j].rank]=1;
        }
        std::sort(a+1,a+1+n,X());
        
        for(i=1;i<=n;i++) answer[i]=0;
        for(i=1;i<=n;i++) check[i]=0;
        path[1]=1;
        f(1,1,1);
        
        printf("Case #%d: ",I);
        for(i=1;i<=n;i++) printf("%d",a[answer[i]].zip);
        //for(i=1;i<=n;i++) printf("%d",answer[i]);
        printf("\n");
        
    }
}
