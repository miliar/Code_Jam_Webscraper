#include<bits/stdc++.h>
using namespace std;
const int N=10100,M=202000,Inf=1<<20,L1=1100,L2=11000;
int n,m,S=0,T=0,dis[N]={};
int nlast[N]={},last[N]={},next[M]={},end[M]={},f[M]={},total_edge=1;
char buf[L1]={},ch[L2]={};
inline void add_edge(int u,int v,int flow)
{
	next[++total_edge]=last[u];
	last[u]=total_edge;
	end[total_edge]=v;
	f[total_edge]=flow;
}
void init()
{
	fill(last,last+N,0);
	total_edge=1;
	gets(buf);
	sscanf(buf,"%d",&n);
	S=0,T=1;
	
	map<string,int> m;
	int tot=0;
	
	for(int t=1;t<=n;++t)
	{
		gets(ch+1);
		int l=strlen(ch+1);
		ch[++l]=' ';
		string s;
		vector<int> v;
		for(int i=1;i<=l;++i)
			if(ch[i]==' ')
			{
				if(!m.count(s))
				{
					m[s]=++tot;
					add_edge(tot*2,tot*2+1,1),add_edge(tot*2+1,tot*2,0);
				}
				int now=m[s];
				v.push_back(now);
				if(t==1)
					add_edge(now*2+1,T,Inf),add_edge(T,now*2+1,0);
				if(t==2)
					add_edge(S,now*2,Inf),add_edge(now*2,S,0);
				s.clear();
			}
			else
				s=s+ch[i];
		if(t>=3)
			for(int i=0;i<(int)v.size();++i)
				for(int j=0;j<(int)v.size();++j)
					add_edge(v[i]+v[i]+1,v[j]+v[j],Inf),add_edge(v[j]+v[j],v[i]+v[i]+1,0);
	}
}
bool bfs()
{
	int q[N]={},head=0,tail=0;
	bool v[N]={};
	q[++tail]=T;
	dis[T]=0;
	v[T]=true;
	while(head!=tail)
		for(int s=q[++head],i=last[s];i;i=next[i])
		{
			int j=end[i];
			if(f[i^1] && !v[j])
				v[j]=true,dis[j]=dis[s]+1,q[++tail]=j;
		}
	return v[S];
}
int dinic(int s,int flow)
{
	if(s==T)
		return flow;
	int x=flow;
	for(int &i=nlast[s];i;i=next[i])
	{
		int j=end[i];
		if(dis[s]==dis[j]+1 && f[i])
		{
			int a=dinic(j,min(x,f[i]));
			f[i]-=a;
			f[i^1]+=a;
			if((x-=a)==0)
				return flow;
		}
	}
	return flow-x;
}
int maxflow()
{
	int ans=0;
	while(bfs())
	{
		copy(last,last+N,nlast);
		ans+=dinic(S,Inf);
	}
	return ans;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	gets(buf);
	sscanf(buf,"%d",&T);
	for(int t=1;t<=T;++t)
	{
		init();
		printf("Case #%d: %d\n",t,maxflow());
	}
	return 0;
}
