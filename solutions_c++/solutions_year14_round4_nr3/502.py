#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <queue>
#define MXN  500010/////
#define MXM 2000100///
#define INF (1<<30)
using namespace std; 
int map[510][510];
int num1[510][510],num2[510][510];
int W,H,b;
struct elist{
     int v,w,inv,last;
}e[MXM];
int n,m,S,T,N,total,etot,zh[MXN],h[MXN],w[MXN];
queue <int> q;
inline void eadd(int u,int v,int w){
	//printf("%d %d %d\n",u,v,w);
     e[++etot].v=v;e[etot].w=w;e[etot].inv=etot+1;e[etot].last=zh[u];zh[u]=etot;
     e[++etot].v=u;e[etot].w=0;e[etot].inv=etot-1;e[etot].last=zh[v];zh[v]=etot;
}
inline void Init(){
    for(int i=1;i<=N;i++) zh[i]=0;etot=0;
    int i,j,k,xs,xt,ys,yt;
    scanf("%d%d%d",&W,&H,&b);
    memset(map,0,sizeof(map));
    for(i=1;i<=b;++i)
    {
		scanf("%d%d%d%d",&xs,&ys,&xt,&yt);
		for(j=xs;j<=xt;++j)
		for(k=ys;k<=yt;++k)
		map[j][k]=1;
	}
	N=2;
	S=1;
	T=2;
	for(i=0;i<W;++i)
		for(j=0;j<H;++j)
			num1[i][j]=++N;
	for(i=0;i<W;++i)
		for(j=0;j<H;++j)
			num2[i][j]=++N;
	for(i=0;i<W;++i)
		for(j=0;j<H;++j)
			if(map[i][j]==0)
				eadd(num1[i][j],num2[i][j],1);
	for(i=0;i<W;++i)
		for(j=0;j<H;++j)
			if(map[i][j]==0)
			{
				if(i-1>=0)
					eadd(num2[i][j],num1[i-1][j],1);
				if(i+1<W)
					eadd(num2[i][j],num1[i+1][j],1);
				if(j-1>=0)
					eadd(num2[i][j],num1[i][j-1],1);
				if(j+1<H)
					eadd(num2[i][j],num1[i][j+1],1);
			}
	for(i=0;i<W;++i)
	{
		if(map[i][0]==0)
			eadd(1,num1[i][0],1);
		if(map[i][H-1]==0)
			eadd(num2[i][H-1],2,1);
	}
}
inline bool bfs(int uu){
     int u;
     memset(h,0,sizeof(h));
     u=uu;q.push(u);
     h[u]=1;//
     while(!q.empty()){
       u=q.front();q.pop();
       for(int i=zh[u];i;i=e[i].last) if(e[i].w&&!h[e[i].v]){
         h[e[i].v]=h[u]+1;
         q.push(e[i].v);
       }
     }
     return h[n+m+2]>0;
}
int maxflow(int u,int lmt){
     if(u==T) return lmt;
     int rest=lmt;//
     for(int i=zh[u];i;i=e[i].last)if(e[i].w&&h[e[i].v]==h[u]+1){////
        int tmp=maxflow(e[i].v,min(e[i].w,rest));/////
        e[i].w-=tmp;e[e[i].inv].w+=tmp;
        rest-=tmp;
     }
     if(rest==lmt) h[u]=INF;//
     return lmt-rest;
}
inline void solve(){
    total=0;
     while(bfs(S)) total+=maxflow(S,INF);/////
}
int main(){
	freopen("124.in","r",stdin);
	freopen("124.out","w",stdout);
	int t,tt;
	scanf("%d",&t);
	for(tt=1;tt<=t;++tt)
	{
    	Init();
    	solve();
     printf("Case #%d: %d\n",tt,total);
	}
    return 0;
}
