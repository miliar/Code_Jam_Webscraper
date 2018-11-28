#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define ll long long
#define LIM 1010
int parent[LIM];
int Rank[LIM];
int val[LIM];
int find(int cur)
{
	if(parent[cur]==cur)
		return cur;
	return parent[cur]=find(parent[cur]);
}

bool Union(int x,int y)
{
	int xroot=find(x);
	int yroot=find(y);
	if(xroot==yroot)
		return false;
	if(Rank[xroot]<Rank[yroot])
		swap(xroot,yroot);
	
	parent[yroot]=xroot;
	val[xroot]+=val[yroot];
	val[yroot]=0;
	if(Rank[xroot]==Rank[yroot])
		Rank[xroot]++;
	if(val[xroot]==2)
		return true;
	return false;
}
void init(int n)
{
	int i;
	for(i=0;i<=n;++i)
	{
		Rank[i]=0;
		parent[i]=i;
		val[i]=0;
	}
}
vector<pair<int,pair<int,int> > > e;
int x[1010],y[1010],z[1010];
int dist(int i,int j)
{
	return ((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])+(z[i]-z[j])*(z[i]-z[j]));
}
int main()
{
	// freopen("C.in","r",stdin);
	// freopen("C.out","w",stdout);
	int t,n,s,i,j;
	sd(t);
	for(int tt=1;tt<=t;tt++)
	{
		e.clear();
		sd(n);
		sd(s);
		for(i=0;i<n;++i)
		{
			int v;
			sd(x[i]);
			sd(y[i]);
			sd(z[i]);
			sd(v);
			sd(v);
			sd(v);
		}
		init(n);
		val[0]=val[1]=1;
		for(i=0;i<n;++i)
			for(j=i+1;j<n;++j)
				e.PB(MP(dist(i,j),MP(i,j)));
		sort(e.begin(),e.end());
		int ans;
		for(i=0;i<e.size();++i)
		{
			if(Union(e[i].S.F,e[i].S.S))
			{
				ans=e[i].F;
				break;
			}
		}
		printf("Case #%d: %.9lf\n",tt,sqrt((double)ans));
	}
}