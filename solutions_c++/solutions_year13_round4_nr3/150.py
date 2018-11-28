#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int Maxn=2100;
const int Maxm=4000000*2;

int date[Maxm],next[Maxm],type[Maxm];
int pos[Maxn];
int a[Maxn],b[Maxn];
int n,m,tot;
bool use[Maxn];
bool visit[Maxn];
int stack[Maxn];
bool find1;
int L[Maxn],R[Maxn];
int q[Maxn];
int f[Maxn];

void Add(int x,int y,int z)
{
	++tot;
	next[tot]=pos[x];pos[x]=tot;
	date[tot]=y;type[tot]=z;
}

bool Check1(int x)
{
	int u=1;
	for (int i=1;i<x;++i)
		if (stack[i]<stack[x] && a[i]+1>u)
			u=a[i]+1;
	return u==a[x];
}

bool Check2()
{
	f[n]=1;
	for (int i=n-1;i>=1;--i)
	{
		f[i]=1;
		for (int j=i+1;j<=n;++j)
			if (stack[j]<stack[i] && f[j]+1>f[i])
				f[i]=f[j]+1;
		if (f[i]!=b[i]) return false;
	}
	return true;
}

void Dfs(int x)
{
	if (x==n+1)
	{
		if (Check2())
		{
			find1=true;
			for (int j=1;j<=n;++j) printf(" %d",stack[j]);
			printf("\n");
			return;
		}
	}
	
	int LL=L[x],RR=R[x];
	int l,r;
	for (l=1;LL>0 && l<=n;++l)
		if (!use[l]) --LL;
	for (r=n;RR>0 && r>0;--r)
		if (!use[r]) --RR;
	
	for (int i=l;i<=r;++i)
		if (!use[i])
		{
			stack[x]=i;
			if (Check1(x))
			{
				use[i]=true;
				Dfs(x+1);
				use[i]=false;
			}
			if (find1) return;
		}
}

void Bfs(int s,int t)
{
	int l1=1,l2=1;
	q[1]=s;
	memset(visit,false,sizeof(visit));
	visit[s]=true;
	for (;l1<=l2;++l1)
	{
		int now=q[l1];
		for (int k=pos[now];k;k=next[k])
		{
			if (type[k]!=t) continue;
			int nex=date[k];
			if (!visit[nex])
			{
				visit[nex]=true;
				q[++l2]=nex;
			}
		}
	}
}

int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	
	int Test;
	scanf("%d",&Test);
	for (int ii=0;ii<Test;++ii)
	{
		printf("Case #%d:",ii+1);
		scanf("%d",&n);
		for (int i=1;i<=n;++i) scanf("%d",&a[i]);
		for (int i=1;i<=n;++i) scanf("%d",&b[i]);
		
		tot=0;
		memset(pos,0,sizeof(pos));
		for (int i=0;i<n;++i)
		{
			int cnt=0;
			for (int j=0;j<i;++j) 
			{
				if (a[j]>=a[i]) Add(j,i,0),Add(i,j,1);
				if (a[j]==a[i]-1) ++cnt;
			}
			if (cnt==1)
				for (int j=0;j<i;++j)
					if (a[j]==a[i]-1) Add(i,j,0),Add(j,i,1);
		}
		for (int i=0;i<n;++i)
		{
			int cnt=0;
			for (int j=i+1;j<n;++j)
			{
				if (b[j]>=b[i]) Add(j,i,0),Add(i,j,1);
				if (b[j]==b[i]-1) ++cnt;
			}
			if (cnt==1)
				for (int j=i+1;j<n;++j)
					if (b[j]==b[i]-1) Add(i,j,0),Add(j,i,1);
		}
		
		for (int x=1;x<=n;++x)
		{
			L[x]=0,R[x]=0;
			Bfs(x,0);
			for (int i=x+1;i<n;++i)
				if (visit[i]) ++L[x];
		
			Bfs(x,1);
			for (int i=x+1;i<n;++i)
				if (visit[i]) ++R[x];
		}
		memset(use,false,sizeof(use));
		find1=false;
		Dfs(1);
	}
	
	return 0;
}
		