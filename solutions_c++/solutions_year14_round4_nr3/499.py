#include<cstdio>
#include<algorithm>
#include<iostream>
#include<vector>
#include<queue>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
using namespace std;

int t,w,h,b,tab[1000][1000],x1,x2,y1,y2,wyn,k,j,g[4]={0,1,0,-1},d[4]={-1,0,1,0};

int dfs(int k,int j,int kier){
    int newk,newj;
    kier=(kier+3)%4;
    //printf("%d %d\n",k,j);
    if(k==h) return 1;
    if(j==w) return 0;
    tab[k][j]=1;
    for(int i=0;i<4;i++){
        newk=k+g[(kier+i)%4];
        newj=j+d[(kier+i)%4];
        //printf("\\%d %d\n",newk,newj);
        if(newj>=0 && newk>=0 && !tab[newk][newj] && dfs(newk,newj,(kier+i)%4)) return 1;
    }
    return 0;
}
    

int main(){
    scanf("%d",&t);
    for(int ttt=1;ttt<=t;ttt++){
        scanf("%d%d%d",&w,&h,&b);
        for(int l=0;l<=h;l++) for(int j=0;j<=w;j++) tab[l][j]=0;
        for(int i=0;i<b;i++){
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for(int j=x1;j<=x2;j++) for(int k=y1;k<=y2;k++) tab[k][j]=1;
        }
        /*for(int l=0;l<h;l++){
            for(int j=0;j<w;j++) printf("%d ",tab[l][j]);
            printf("\n");
        }*/
        wyn=0;
        for(int i=0;i<w;i++){
            k=0;
            j=i;
            if(tab[k][j]==0) wyn+=dfs(k,j,1);
        }
        printf("Case #%d: %d\n",ttt,wyn);
    }

}

