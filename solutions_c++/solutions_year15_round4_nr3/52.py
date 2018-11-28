#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <list>
#include <queue>
#include <vector>
#include <ctime>
#include <set>
#include <bitset>
#include <deque>
#include <fstream>
#include <stack>
#include <map>
#include <utility>
#include <cassert>
#include <string>
#include <iterator>
#include <cctype>
using namespace std;
typedef long long LL;
double getd()
{
    double d=0,d2=0,d3=1; char ch; bool flag=0;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')flag=true;else d=ch-48;
    while(isdigit(ch=getchar()))d=d*10+ch-48;
    if(ch=='.')
    {
        while(isdigit(ch=getchar()))d2=d2*10+ch-48,d3=d3*0.1;
        d+=d3*d2;
    }
    if(flag)return -d;else return d;
}
int get()
{
    int f=0,v=0;char ch;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')f=1;else v=ch-48;
    while(isdigit(ch=getchar()))v=v*10+ch-48;
    if(f==1)return -v;else return v;
}
const int maxn=500003;
const int maxm=500003;
const int inf=5000,INF=1000000000;
struct Tedge
{
	int t,v,op,pre;
	Tedge(){}
	Tedge(int _t,int _v,int _op,int _pre){t=_t,v=_v,op=_op,pre=_pre;}
}g[maxm];
int n,source,sink,Link[maxn],s[maxn],h[maxn],tot,fst[maxn];
inline void add(int s,int t,int v)
{
	//cout<<s<<" "<<t<<" "<<v<<endl;
	int tp;
	tp=Link[s]; Link[s]=++tot; g[tot]=Tedge(t,v,tot+1,tp);
	tp=Link[t]; Link[t]=++tot; g[tot]=Tedge(s,0,tot-1,tp);
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
		d=min(tp,g[i].v);
		d=aug(g[i].t,d);
		g[i].v-=d,g[g[i].op].v+=d,tp-=d;
		if(tp==0)break;
	}
	fst[x]=i;
	if(tp==flow)h[x]=-1;
	return flow-tp;
}
const int seed=13313,mod=1000000007;
char ss[100];
int Tdic;
vector<int> sen[maxn];
map<LL,int> dic;
int main()
{
	freopen("Cl.in","r",stdin);
	freopen("Cl.out","w",stdout);
	int T=get();
	for(int _=1;_<=T;_++)
	{
		scanf("%d",&n);
		dic.clear();Tdic=0;
		for(int i=1;i<=n;i++)
		{
			sen[i].clear();
			while(1)
			{
				scanf("%s",ss+1);
				LL hash=0;int ll=strlen(ss+1);
				for(int j=1;j<=ll;j++)hash=(hash*seed+ss[j])%mod;
				if(!dic.count(hash))dic[hash]=++Tdic;
				sen[i].push_back(dic[hash]);
				char ch=getchar();
				if(ch!=' ')break;
			}
		}
		memset(Link,0,sizeof(Link)),tot=0;
		source=2*n+2*Tdic+1;sink=source+1;
		add(source,1,inf),add(1+n,sink,INF);
		add(source,2,INF),add(2+n,sink,inf);
		for(int i=1;i<=Tdic;i++)add(i+2*n,i+Tdic+2*n,1);
		for(int i=1;i<=n;i++)
		{
			if(i>2)
			{
				add(source,i,inf),add(i+n,sink,inf);
			}
			add(i,i+n,INF);
			for(int j=0;j<(int)sen[i].size();j++)
			{
				int k=sen[i][j];
				add(i,k+2*n,INF),add(k+Tdic+2*n,i+n,INF);
			}
		}
		int ans=0;
		while(bfs())ans+=aug(source,INF+10);
		printf("Case #%d: %d\n",_,ans-inf*n);
	}
	return 0;
}
