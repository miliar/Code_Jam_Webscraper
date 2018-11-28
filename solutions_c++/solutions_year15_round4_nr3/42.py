/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>
#include<cassert>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
typedef unsigned int uint;
#define pb push_back
#define fi first
#define se second
#define mp make_pair

const int MOD=1000000007,dx[]={0,1,0,-1},dy[]={1,0,-1,0};
const double eps=1e-8;

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

int Tot,n,ind,S,T;
map<string,int> A;

const int MAXN=2*4000+20;
const int MAXM=5000000;
const int inf=1000000000;

struct graph
{
	int a[MAXN],b[MAXM],c[MAXM],d[MAXM],p,h[MAXN],dd[MAXN],ll,rr;
	void clear()
	{
		memset(a,0,sizeof a);
		p=1;
	}
	void addedge(int x,int y,int z)
	{
		//printf("%d %d %d\n",x,y,z);
		c[++p]=a[x]; a[x]=p; b[p]=y; d[p]=z;
		c[++p]=a[y]; a[y]=p; b[p]=x; d[p]=0;
		assert(p<MAXM);
	}
	bool bfs()
	{
		memset(h,0,sizeof h);
		for(h[dd[ll=rr=0]=T]=1;ll<=rr;ll++)
			for(int i=a[dd[ll]];i;i=c[i]) if (d[i^1]&&!h[b[i]])
				h[dd[++rr]=b[i]]=h[dd[ll]]+1;
		return h[S];
	}
	int dfs(int k,int now)
	{
		if (h[k]==1) return now;
		int tt=now;
		for(int i=a[k];i;i=c[i]) if (d[i]&&h[k]==1+h[b[i]])
		{
			int o=dfs(b[i],min(now,d[i]));
			now-=o; d[i]-=o; d[i^1]+=o;
			if (!now) break;
		}
		if (tt==now) h[k]=2000000000;
		return tt-now;
	}
	int maxflow()
	{
		int ret=0;
		for(;bfs();)
			ret+=dfs(S,inf);
		return ret;
	}
} B;

int C[2010][2010];

void try_add(int x,int y)
{
	assert(x<=2000 && y<=2000);
	if (!C[x][y])
	{
		C[x][y]=1;
		B.addedge(x+ind,y,inf);
	}
}

vector<int> sto[4010];

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	cin>>Tot;
	for(int tt=1;tt<=Tot;tt++)
	{
		cin>>n;
		A.clear();
		B.clear();
		ind=0;
		string s,t;
		getline(cin,s);
		for(int i=0;i<n;i++)
		{
			getline(cin,s);
			istringstream sin(s);
			sto[i].clear();
			while(sin>>t)
			{
				if (!A.count(t)) A[t]=++ind;
				sto[i].push_back(A[t]);
			}
		}
		S=2*ind+1;
		T=2*ind+2;
		for(int i=1;i<=ind;i++)
			B.addedge(i,i+ind,1);
		memset(C,0,sizeof C);
		for(int i=2;i<n;i++)
			for(int j=0,l=sto[i].size();j<l;j++)
				for(int k=j+1;k<l;k++)
				{
					try_add(sto[i][j],sto[i][k]);
					try_add(sto[i][k],sto[i][j]);
					//B.addedge(sto[i][j]+ind,sto[i][k],inf);
					//B.addedge(sto[i][k]+ind,sto[i][j],inf);
				}
		for(int j=0,l=sto[0].size();j<l;j++)
			B.addedge(S,sto[0][j],inf);
		for(int j=0,l=sto[1].size();j<l;j++)
			B.addedge(sto[1][j]+ind,T,inf);
		printf("Case #%d: %d\n",tt,B.maxflow());
	}
	
	return 0;
}
