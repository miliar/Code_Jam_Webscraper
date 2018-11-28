#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <ctime>
#include <set>
#include <bitset>
#include <map>
#include <utility>
#include <iterator>
using namespace std;
inline int get()
{
    int f=0,v=0;char ch;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')f=1;else v=ch-48;
    while(isdigit(ch=getchar()))v=v*10+ch-48;
    if(f==1)return -v;else return v;
}
const int maxn=103*503*2,maxm=4020000,inf=1000000000;
const int dx[]={0,0,-1,1},dy[]={1,-1,0,0};
struct Tedge
{
	int t,v,op,pre;
	Tedge(){}
	Tedge(int _t,int _v,int _op,int _pre){t=_t,v=_v,op=_op,pre=_pre;}
}g[maxm];
int n,m,K,source,sink,Link[maxn],s[maxn],h[maxn],ans=0,tot=0,fst[maxn],a[555][555],idS[555][555],idT[555][555];
inline void add(int s,int t,int v)
{
	int tp;
	tp=Link[s]; Link[s]=++tot; g[tot]=Tedge(t,v,tot+1,tp);
	tp=Link[t]; Link[t]=++tot; g[tot]=Tedge(s,0,tot-1,tp);
//	cout<<s<<" "<<t<<" "<<v<<endl;
}
inline bool bfs()
{
	for(int i=1;i<=sink;i++)h[i]=-1,fst[i]=Link[i];
	int front=0,rear=1;
	s[front]=source,h[source]=1;
	while(front!=rear)
	{
		int p=s[front];
		for(int i=Link[p];i;i=g[i].pre)
			if(h[g[i].t]==-1&&g[i].v)h[g[i].t]=h[p]+1,s[rear++]=g[i].t;
		front++;
	}
	return h[sink]!=-1;
}
inline int aug(int x,int flow)
{
	if(x==sink)return flow;
	int tp=flow,d,i;
	for(i=fst[x];i;i=g[i].pre)
	{
		if(h[g[i].t]!=h[x]+1||g[i].v<=0)continue;
		d=min(tp,g[i].v),d=aug(g[i].t,d);
		g[i].v-=d,g[g[i].op].v+=d,tp-=d;
		if(tp==0)break;
	}
	fst[x]=i;
	if(tp==flow)h[x]=-1;
	return flow-tp;
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int T=get();
    for(int t=1;t<=T;t++)
    {
		cerr<<t<<endl;
		n=get(),m=get();K=get();
		memset(a,255,sizeof(a));
		memset(Link,0,sizeof(Link));tot=0;
		int cnt=0;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)idS[i][j]=++cnt;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)idT[i][j]=++cnt;
		source=cnt+1,sink=source+1;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)a[i][j]=0;
		for(int i=1;i<=K;i++)
		{
			int x1=get()+1,y1=get()+1,x2=get()+1,y2=get()+1;
			for(int x=x1;x<=x2;x++)
				for(int y=y1;y<=y2;y++)a[x][y]=-1;
		}
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
			{
				if(a[i][j]==-1)continue;
				add(idS[i][j],idT[i][j],1);
				for(int k=0;k<4;k++)
				{
					int xx=i+dx[k],yy=j+dy[k];
					if(a[xx][yy]==-1)continue;
					add(idT[i][j],idS[xx][yy],inf);
				}
			}
		for(int i=1;i<=n;i++)
		{
			if(a[i][1]!=-1)add(source,idS[i][1],1);
			if(a[i][m]!=-1)add(idT[i][m],sink,inf);
		}
		int ans=0;
		while(bfs())ans+=aug(source,inf);
		if(sink>maxn){cerr<<"!"<<endl;while(1);}
		if(tot>maxm){cerr<<"!"<<endl;while(1);}
		printf("Case #%d: %d\n",t,ans);
	}
    return 0;
}
