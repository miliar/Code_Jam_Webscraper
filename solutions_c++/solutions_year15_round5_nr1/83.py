#include<bits/stdc++.h>
using namespace std;
const int N=1000100;
struct node
{
	int l,r,lazy,s;
}t[N<<2]={};
void make_tree(int l,int r,int k)
{
	if(l!=r)
	{
		int mid=(l+r)>>1;
		make_tree(l,mid,k<<1);
		make_tree(mid+1,r,(k<<1)|1);
	}
	t[k].l=l,t[k].r=r;
	t[k].lazy=0;
	t[k].s=r-l+1;
}
void update(int k)
{
	if(t[k].lazy)
		t[k].s=0;
	else
		if(t[k].l!=t[k].r)
			t[k].s=t[k<<1].s+t[(k<<1)|1].s;
		else
			t[k].s=1;
}
void add_lazy(int k,int c)
{
	t[k].lazy+=c;
	update(k);
}
void add(int l,int r,int c,int k)
{
	if(t[k].l>=l && t[k].r<=r)
		return add_lazy(k,c);
	if(t[k<<1].r>=l)
		add(l,r,c,k<<1);
	if(t[(k<<1)|1].l<=r)
		add(l,r,c,(k<<1)|1);
	update(k);
}
int n,d,last[N]={},end[N+N]={},next[N+N]={},total_edge=0;
int l[N]={},r[N]={},tot=0;
inline void add_edge(int u,int v)
{
	next[++total_edge]=last[u];
	last[u]=total_edge;
	end[total_edge]=v;
}
struct employee
{
	int f,v,num;
}e[N]={};
bool cmp(const employee &e1,const employee &e2)
{
	return e1.v<e2.v;
}
void dfs(int s)
{
	l[s]=++tot;
	for(int i=last[s];i;i=next[i])
	{
		int j=end[i];
		if(j==e[s].f)
			continue;
		dfs(j);
	}
	r[s]=tot;
}
void init()
{
	cin>>n>>d;
	total_edge=tot=0;
	fill(last+1,last+n+1,0);
	long long s0,as,cs,rs,m0,am,cm,rm;
	cin>>s0>>as>>cs>>rs>>m0>>am>>cm>>rm;
	e[1]=(employee){0,s0,1};
	for(int i=2;i<=n;++i)
	{
		s0=(s0*as+cs)%rs;
		m0=(m0*am+cm)%rm;
		//cout<<"s0="<<s0<<" m0="<<m0<<endl;
		int f=m0%(i-1)+1;
		add_edge(f,i);
		e[i]=(employee){f,s0,i};
	}
	dfs(1);
	sort(e+1,e+n+1,cmp);
}
void work()
{
	make_tree(1,n,1);
	for(int i=1;i<=n;++i)
		add(l[i],r[i],1,1);
	int p1=1,ans=0;
	//for(int i=1;i<=n;++i)
	//	cout<<e[i].f<<' '<<e[i].v<<' '<<e[i].num<<endl;
	for(int i=1;i<=n;++i)
	{
		while(p1<=n && e[p1].v-e[i].v<=d)
		{
			add(l[e[p1].num],r[e[p1].num],-1,1);
			++p1;
		}
		//cout<<"i="<<i<<" p1="<<p1<<" s="<<t[1].s<<endl;
		ans=max(ans,t[1].s);
		add(l[e[i].num],r[e[i].num],1,1);
	}
	cout<<ans<<endl;
}
int main()
{	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		init();
		cout<<"Case #"<<t<<": ";
		work();
	}
	return 0;
}
