//
//  main.cpp
//  Round 1C 2014. Problem C. Enclosure
//
//  Created by kimtaeyang on 2014. 5. 11..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//


#include <stdio.h>

int n,m,k;
int a[100][100];
int answer;
int e[4][2]={-1,0,1,0,0,-1,0,1};

int check(){
    a[0][0]=2;
    int queue[10000][2],N;
    N=1; queue[1][0]=0; queue[1][1]=0;
    int i,j,x,y;
    for(i=1;i<=N;i++){
        x=queue[i][0];
        y=queue[i][1];
        for(j=0;j<4;j++) if(0<=x+e[j][0] && x+e[j][0]<=n+1 && 0<=y+e[j][1] && y+e[j][1]<=m+1 && !a[x+e[j][0]][y+e[j][1]]){
            queue[++N][0]=x+e[j][0];
            queue[N][1]=y+e[j][1];
            a[x+e[j][0]][y+e[j][1]]=2;
        }
    }
    int count=0;
    for(i=1;i<=n;i++) for(j=1;j<=m;j++) if(a[i][j]!=2) count++;
    for(i=0;i<=n+1;i++) for(j=0;j<=m+1;j++) if(a[i][j]==2) a[i][j]=0;
    return count;
}

void f(int x, int y, int z){
    if(x==n+1){
        if(check()>=k && z<=answer) answer=z;
        return ;
    }
    if(y==m+1){f(x+1,1,z); return;}
    a[x][y]=1; f(x,y+1,z+1);
    a[x][y]=0; f(x,y+1,z);
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T,I;
    
    scanf("%d",&T);
    for(I=1;I<=T;I++){
        scanf("%d%d%d",&n,&m,&k);
        answer=n*m;
        f(1,1,0);
        printf("Case #%d: %d\n",I,answer);
        
    }
    
}

