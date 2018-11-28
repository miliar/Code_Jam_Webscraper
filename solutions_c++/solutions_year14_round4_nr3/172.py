#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#define oo 1000000000
#define aabs(x) ((x)<0?(-(x)):(x))
using namespace std;
struct data{
    int x0,y0,x1,y1;
}A[1005];
int G[1005][1005];
int Hash[1005],Dis[1005];
void Up(int &x,int y){
    if(x>y)x=y;
}
int Do(int p,int q){
    int x,y;
    if(A[p].x0>A[q].x1)x=A[p].x0-A[q].x1-1;
    else if(A[p].x1<A[q].x0)x=A[q].x0-A[p].x1-1;
    else x=0;
    if(A[p].y0>A[q].y1)y=A[p].y0-A[q].y1-1;
    else if(A[p].y1<A[q].y0)y=A[q].y0-A[p].y1-1;
    else y=0;
    return max(x,y);
}
int main(){
    int T,tt=0,B,H,W,n,i,j,k,l;
    scanf("%d",&T);
    freopen("C.out","w",stdout);
    while(T--){

        scanf("%d%d%d",&W,&H,&n);
        for(i=1;i<=n;i++){
            scanf("%d%d%d%d",&A[i].x0,&A[i].y0,&A[i].x1,&A[i].y1);
        }
        n++;
        A[n].x0=-1;
        A[n].y0=-1;
        A[n].x1=-1;
        A[n].y1=H;
        n++;
        A[n].x0=W;
        A[n].y0=-1;
        A[n].x1=W;
        A[n].y1=H;
        for(i=1;i<=n;i++){
            for(j=i+1;j<=n;j++){
                G[i][j]=Do(i,j);
                G[j][i]=G[i][j];
            }
            G[i][i]=0;
        }
        memset(Hash,0,sizeof(Hash));
        for(i=1;i<=n;i++)Dis[i]=oo;
        Dis[n]=0;
        for(i=1;i<=n;i++){
            k=oo;l=0;
            for(j=1;j<=n;j++)
                if(!Hash[j]&&Dis[j]<k){k=Dis[j];l=j;}
   // printf("%d %d\n",l,Dis[l]);
   // printf("%d\n",G[3][5]);
            if(l==0)break;
            Hash[l]=1;
            for(j=1;j<=n;j++)
                if(Dis[j]>Dis[l]+G[l][j])Dis[j]=Dis[l]+G[l][j];
        }
        tt++;
        printf("Case #%d: %d\n",tt,Dis[n-1]);
    }
    return 0;
}
