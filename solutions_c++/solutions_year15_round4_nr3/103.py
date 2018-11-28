#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<bitset>
using namespace std;
typedef long long ll;
typedef double db;
const db pi=acos(-1);
void gn(int &x){
	int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');
	if(c=='-')sg=-1,x=0;else x=c-'0';
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';
	x*=sg;
}
void gn(ll &x){
	int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');
	if(c=='-')sg=-1,x=0;else x=c-'0';
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';
	x*=sg;
}
const int mo=1000000007;
int qp(int a,ll b){int ans=1;do{if(b&1)ans=1ll*ans*a%mo;a=1ll*a*a%mo;}while(b>>=1);return ans;}
////////////////////////////////////
typedef int nu;
const nu inf=1000000000;
const int MAXV=111111+5;
const int MAXE=2500000+5;
////////////////////////////////////
int s,t;
struct edge{int v,next;nu f;}e[MAXE*2];int g[MAXV],etot;
void ae(int u,int v,nu f){
	e[etot].v=v;e[etot].f=f;e[etot].next=g[u];g[u]=etot++;
	e[etot].v=u;e[etot].f=0;e[etot].next=g[v];g[v]=etot++;
}
int d[MAXV],qu[MAXV];
int lb(){
	for (int i=1;i<=t;i++)d[i]=0;
	int p=0,q=0;
	qu[q++]=s,d[s]=1;
	while(p!=q){
		int u=qu[p++];
		for (int i=g[u];~i;i=e[i].next)if(e[i].f && !d[e[i].v]){
			d[e[i].v]=d[u]+1;
			if(e[i].v==t)return 1;
			qu[q++]=e[i].v;
		}
	}return 0;
}
nu aug(int u,nu mi){
	if(u==t)return mi;
	nu su=0,del;
	for (int i=g[u];~i;i=e[i].next)if(e[i].f && d[e[i].v]==d[u]+1){
		del=aug(e[i].v,min(mi,e[i].f));
		mi-=del;
		e[i].f-=del;e[i^1].f+=del;
		su+=del;
		if(!mi)break;
	}
	if(!su)d[u]=-1;
	return su;
}
nu dinic(){
	nu su=0;
	while(lb())su+=aug(s,inf);
	return su;
}
void init(){
	etot=0;
	memset(g,-1,sizeof(g));
}

int n;
char ss[1111];
int get(char *s){
	char c;
	int tot=0;
	while((c=getchar())<'a'||c>'z');
	s[tot++]=c;
	while((c=getchar())>='a'&&c<='z')s[tot++]=c;
	s[tot++]=0;
	return c!=' ';
}
ll gethas(char *s){
	ll ha=0;
	for (int i=0;s[i];i++)ha=ha*10007+s[i];
	return ha;
}

ll ls[222][11111];int len[222];
map<ll,int>ma;
void glin(int i){
	int tot=0;
	while(!get(ss)){
		ls[i][++tot]=gethas(ss);
		ma[ls[i][tot]];
	}
	ls[i][++tot]=gethas(ss);
	ma[ls[i][tot]];
	len[i]=tot;
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("2.out","w",stdout);
	int tes;scanf("%d",&tes);
	for (int tt=1;tt<=tes;tt++){
		ma.clear();
		init();
		scanf("%d",&n);
		printf("Case #%d: ",tt);
		for (int i=1;i<=n;i++)
			glin(i);
		int wtot=0;
		for(map<ll,int>::iterator it = ma.begin();it!=ma.end();it++)it->second=++wtot;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=len[i];j++)ls[i][j]=ma[ls[i][j]];
		s=n+wtot*2+1,t=s+1;
		ae(1+wtot*2,t,inf);
		ae(s,2+wtot*2,inf);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=len[i];j++){
				ae(ls[i][j]+wtot,i+wtot*2,inf);
				ae(i+wtot*2,ls[i][j],inf);
			}
		for (int i=1;i<=wtot;i++)ae(i,i+wtot,1);
		printf("%d\n",dinic());
	}
	return 0;
}

