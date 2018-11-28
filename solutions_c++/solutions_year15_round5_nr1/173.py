#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cassert>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
struct enode{int to,next;}mye[1000001];
int first[1000001];
bool active[1000001];bool die[1000001];
int salary[1000001];int parent[1000001];
int idx[1000001];
bool cmp(int ia,int ib)
{
	return salary[ia]<salary[ib];
}
int n,nd;
int s0,as,cs,rs;
int m0,am,cm,rm;
int dieat;
int tot;
struct people
{
	int n,w;
	bool operator <(people ano)const
	{
		return w<ano.w;
	}
}sorted[1000001];
int current;
void dfs1(int iv)
{
	//cout<<"Ding:"<<iv<<endl;
	if(active[iv])return;
	active[iv]=true;
	++tot;
	for(int p=first[iv];p;p=mye[p].next)
	{
		int pt=mye[p].to;
		if(die[pt]||active[pt])continue;
		//cout<<"Toding:"<<pt<<","<<salary[pt]<<"<="<<salary[iv]<<endl;
		if(salary[pt]<=current)dfs1(pt);
	}
}
void dfs2(int iv)
{
	//cout<<"Ding2:"<<iv<<endl;
	if(die[iv])return;
	if(active[iv])--tot;
	active[iv]=false;
	die[iv]=true;
	for(int p=first[iv];p;p=mye[p].next)
	{
		int pt=mye[p].to;
		if(die[pt])continue;
		dfs2(pt);
	}
}
	
void task()
{
	scanf("%d%d",&n,&nd);
	scanf("%d%d%d%d",&s0,&as,&cs,&rs);
	scanf("%d%d%d%d",&m0,&am,&cm,&rm);
	memset(die,0,sizeof die);
	memset(active,0,sizeof active);
	memset(first,0,sizeof first);
	int si=s0,mi=m0;
	rep(i,n)
	{
		salary[i]=si;
		sorted[i].n=i;
		sorted[i].w=salary[i];
			//cout<<"Adding:"<<i<<","<<si<<endl;
		if(i-1)
		{
			parent[i]=mi%(i-1)+1;
			mye[i].to=i;
			mye[i].next=first[parent[i]];first[parent[i]]=i;
		}
		si=(si*(long long)as+cs)%rs;
		mi=(mi*(long long)am+cm)%rm;
	}
	sort(sorted+1,sorted+n+1);
	/*rep(i,n)
	{
		cout<<idx[i]<<" ";
	}*/
	dieat=1;
	int maxres=1;
	//active[1]=true;tot=1;
	tot=0;
	rep(i,n)
	{
		int iv=sorted[i].n;
		if(die[iv])continue;
		//cout<<"New:"<<iv<<endl;
		if(salary[iv]<salary[1])continue;
		if(iv!=1)if(!active[parent[iv]])continue;
		//cout<<"New:"<<iv<<endl;
		current=salary[iv];
		dfs1(iv);
		while(dieat<=n&&!die[iv]&&salary[iv]-salary[sorted[dieat].n]>nd){dfs2(sorted[dieat].n);++dieat;}
		maxres=max(maxres,tot);
	}
	printf("%d\n",maxres);
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	//task();
	int nt;scanf("%d",&nt);
	rep(it,nt){printf("Case #%d: ",it);task();}
}
