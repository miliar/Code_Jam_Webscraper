#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <sstream>
#include <vector>

using namespace std;

const int MAXN=5010,MAXM=500010;
const int inf=1000000000;

int n,m,s,t;

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
		c[++p]=a[x]; a[x]=p; b[p]=y; d[p]=z;
		c[++p]=a[y]; a[y]=p; b[p]=x; d[p]=0;
	}
	bool bfs()
	{
		for (int i=0;i<=n;++i)
			h[i]=0;
		for(h[dd[ll=rr=0]=t]=1;ll<=rr;ll++)
			for(int i=a[dd[ll]];i;i=c[i]) if (d[i^1]&&!h[b[i]])
				h[dd[++rr]=b[i]]=h[dd[ll]]+1;
		return h[s];
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
		for(;bfs();) ret+=dfs(s,inf);
		return ret;
	}
} a;

int tt;
map<string,int> hash;
int N;
bool b[5010],w[5010];
vector<int> g[210];

int getid(const string &s) {
	int now=hash.size();
	if (hash.find(s)==hash.end()) hash[s]=now;
	return hash[s];
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	cin >> tt;
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d\n",&N);
		string S;
		memset(b,false,sizeof(b));
		memset(w,false,sizeof(w));
		hash.clear();
		{
		getline(cin,S);
		stringstream ss(S);
		while (ss>>S) {
			int k=getid(S);
			b[k]=true;
		}
		}
		{
		getline(cin,S);
		stringstream ss(S);
		while (ss>>S) {
			int k=getid(S);
			w[k]=true;
		}
		}
		for (int i=0;i<N-2;++i) {
			g[i].clear();
			getline(cin,S);
			stringstream ss(S);
			while (ss>>S) {
				int k=getid(S);
				g[i].push_back(k);
			}
		}
		s=1;
		n=hash.size();
		t=s+n+n+1;
		a.clear();
		for (int i=0;i<n;++i) {
			a.addedge(i+2,i+2+n,1);
			a.addedge(i+2+n,i+2,inf);
			if (b[i]) a.addedge(s,i+2,inf);
			if (w[i]) a.addedge(i+2+n,t,inf);
		}

		for (int i=0;i<N-2;++i) {
			int p=g[i].size();
			for (int j=0;j<p;++j)
				for (int k=j+1;k<p;++k) {
					a.addedge(g[i][j]+n+2,g[i][k]+2,inf);
					a.addedge(g[i][k]+n+2,g[i][j]+2,inf);
				}
		}

		n=t;

		printf("Case #%d: %d\n",ii,a.maxflow());
	}

}



