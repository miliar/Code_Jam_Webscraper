#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<ctime>
#include<climits>
#include<complex>
#include<cassert>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) (int)((x).size())
#define all(x) x.begin(),x.end()
#define clr(x) memset((x),0,sizeof(x))
#define cdp(x) memset((x),-1,sizeof(x))
#define rep(i,n) for (i=0;i<n;i++)
#define Rep(i,a,b) for (i=a;i<=b;i++)
#define ff(i,x) for (i=start[x];i!=-1;i=a[i].next)
#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
using namespace std;
const double eps=1e-8;
const double pi=acos(-1.0);
int dblcmp(double d){if (fabs(d)<eps)return 0;return d>eps?1:-1;}
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpi;
const int maxm=1550000;
const int maxn=551000;
const int inf=0x7fffffff;
struct edge
{
    int v,flow,c,next;
}a[maxm*4];
int tot,start[maxn],n,m,s,t;
inline void init()
{
	memset(start,-1,sizeof(start));
	tot=0;
}
void _addedge(int u,int v,int flow)
{
    a[tot].v=v;
    a[tot].flow=a[tot].c=flow;
    a[tot].next=start[u];
    start[u]=tot++;
}
void addedge(int u,int v,int flow)
{
    _addedge(u,v,flow);
    _addedge(v,u,0);
}
int h[maxn],gap[maxn];
inline int dfs(int pos,int cost)
{
	//printf("%d\n",pos);system("pause");
	if (pos==t)
	{
		return cost;
	}
	int i,j,k,mi=n-1,lv=cost,d;
	if(cost==0)return 0;
	for (i=start[pos];i!=-1;i=a[i].next)
	{
		int v=a[i].v,fl=a[i].flow;
		if (fl>0)
		{
			if (h[v]+1==h[pos])
			{
				d=min(fl,lv);
				d=dfs(v,d);
				a[i].flow-=d;
				a[i^1].flow+=d;
				lv-=d;
				if (h[s]>=n)
				{
					return cost-lv;
				}
				if (!lv)break;
			}
			mi=min(mi,h[v]);
		}
	}
	if (lv==cost)
	{
		--gap[h[pos]];
		if (!gap[h[pos]])h[s]=n;
		h[pos]=mi+1;
		++gap[h[pos]];
	}
	return cost-lv;
}
int sap()
{
	memset(gap,0,sizeof(gap));
	memset(h,0,sizeof(h));
	gap[0]=n;
	int ret=0;
	while (h[s]<n)
	{
		ret+=dfs(s,INT_MAX);
	}
	return ret;
}
int mk[555][555],idx[555][555],idx1[555][555];
int main()
{
	freopen("C://competition//R2//C-small-attempt0 (1).in","r",stdin);
	freopen("C://competition//R2//C.out","w",stdout);
	int i,j,k,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		int w,h,b;
		scanf("%d%d%d",&w,&h,&b);
		clr(mk);
		for (i=0;i<b;i++)
		{
			int x0,x2,y0,y2,x,y;
			scanf("%d%d%d%d",&x0,&y0,&x2,&y2);
			for (x=x0;x<=x2;x++)
			{
				for (y=y0;y<=y2;y++)
				{
					mk[x][y]=1;
				}
			}
		}
		int cnt=0;
		init();
		for (i=0;i<w;i++)
		{
			for (j=0;j<h;j++)
			{
				if (!mk[i][j])
				{
					idx[i][j]=cnt++;
					idx1[i][j]=cnt++;
					addedge(idx[i][j],idx1[i][j],1);
				}
			}
		}
		s=cnt++;
		t=cnt++;
		n=cnt;
		for (i=0;i<w;i++)
		{
			if (!mk[i][0])addedge(s,idx[i][0],1);
			if (!mk[i][h-1])addedge(idx1[i][h-1],t,1);
		}
		int dx[]={-1,0,0,1};
		int dy[]={0,1,-1,0};
		for (i=0;i<w;i++)
		{
			for (j=0;j<h;j++)if (!mk[i][j])
			{
				for (k=0;k<4;k++)
				{
					int x=i+dx[k];
					int y=j+dy[k];
					if (x>=0&&x<w&&y>=0&&y<h&&!mk[x][y])
					{
						addedge(idx1[i][j],idx[x][y],1);
					}
				}
			}
		}
		int ans;
		if (b==0)ans=w;
		else ans=sap();
		printf("Case #%d: %d\n",++cc,ans);
	}
	return 0;
}