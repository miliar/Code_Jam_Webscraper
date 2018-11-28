/*
Author: elfness@UESTC
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
using namespace std;
typedef long long LL;
const int V=100100;
const int En=8*V;
const int oo=0x3f3f3f3f;
struct Edge{int num,ne,c;}e[En];
int d[V],p[V],pre[V],low[V];
int gap[V],cur[V];
int N,K,st,ed;
void add(int x,int y,int c)
{
	e[K].num=y;e[K].c=c;
	e[K].ne=p[x];p[x]=K++;
	e[K].num=x;e[K].c=0;
	e[K].ne=p[y];p[y]=K++;
}
int sap()
{
	int ret=0;
	bool fail;
	for(int i=0;i<=N;i++)
	{
		low[i]=gap[i]=d[i]=0;
		cur[i]=p[i];
	}
	low[st]=oo;gap[0]=N;int u=st;
	while(d[st]<N)
	{
		fail=true;
		for(int i=cur[u];i!=-1;i=e[i].ne)
		{
			int v=e[i].num;cur[u]=i;
			if(e[i].c&&d[u]==d[v]+1)
			{
				pre[v]=i;
				low[v]=min(low[u],e[i].c);u=v;
				if(u==ed)
				{
					do
					{
						e[pre[u]].c-=low[ed];
						e[pre[u]^1].c+=low[ed];
						u=e[pre[u]^1].num;
					}while(u!=st);
					ret+=low[ed];
				}
				fail=false;break;
			}
		}
		if(fail)
		{
			gap[d[u]]--;
			if(!gap[d[u]])return ret;
			d[u]=N;
			for(int i=p[u];i!=-1;i=e[i].ne)
			if(e[i].c)d[u]=min(d[u],d[e[i].num]+1);
			gap[d[u]]++;cur[u]=p[u];
			if(u!=st)u=e[pre[u]^1].num;
		}
	}
	return ret;
}
int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};
int _,W,H,B,lx,ly,rx,ry;
int a[110][510];
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&_);
	for(int ca=1;ca<=_;ca++)
	{
		scanf("%d%d%d",&W,&H,&B);
		memset(a,0,sizeof(a));
		for(int i=0;i<B;i++)
		{
			scanf("%d%d%d%d",&lx,&ly,&rx,&ry);
			for(int j=lx;j<=rx;j++)
			for(int k=ly;k<=ry;k++)
			a[j][k]=1;
		}
		N=2*W*H+2;
		st=N-2;ed=N-1;
		memset(p,-1,sizeof(p));K=0;
		for(int i=0;i<W;i++)
		for(int j=0;j<H;j++)
		if(a[i][j]==0)
		{
			int id=i*H+j;
			if(j==0)add(st,id,1);
			if(j==H-1)add(id+W*H,ed,1);
			add(id,id+W*H,1);
			for(int k=0;k<4;k++)
			{
				int tx=i+dx[k];
				int ty=j+dy[k];
				if(tx<0||tx>=W)continue;
				if(ty<0||ty>=H)continue;
				if(a[tx][ty]==1)continue;
				add(W*H+id,tx*H+ty,1);
			}
		}
		cerr<<ca<<endl;
		printf("Case #%d: %d\n",ca,sap());
	}
	return 0;
}
