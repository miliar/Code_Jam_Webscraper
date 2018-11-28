#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<cmath>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<string>
#include<queue>
#include<iomanip>
#include<limits>
#include<typeinfo>
#include<functional>
#include<numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<ld,ld> pdd;

#define X first
#define Y second

	namespace spfa_cost_flow
	{
		template<class type=int> class flow_graph
		{
			private:
				//const type INF=typeid(int)==typeid(type)?1000000000:1000000000000000000LL;
				const static type INF=1000000000;
			public:
				int n,S,T;
			private:
				struct node
				{
					int from,way;
					type cap,cost;
					node *next,*rev;
				};
				node **v;
				type max_flow,ans;
				type *dis;
				node **pre;
				int *used;
				bool SPFA()
				{
					for (int i=1;i<=n;++i)
					{
						dis[i]=INF;
						used[i]=0;
					}
					dis[S]=0;
					queue<int> Q;
					Q.push(S);
					used[S]=1;
					while (!Q.empty())
					{
						int x=Q.front();
						Q.pop();
						used[x]=0;
						for (node *it=v[x];it;it=it->next)
							if (it->cap>0&&dis[it->way]>dis[x]+it->cost)
							{
								dis[it->way]=dis[x]+it->cost;
								pre[it->way]=it;
								if (!used[it->way])
								{
									used[it->way]=1;
									Q.push(it->way);
								}
							}
					}
					if (dis[T]==INF) return 0;
					type flow=INF;
					for (int i=T;i!=S;i=pre[i]->from)
						flow=min(flow,pre[i]->cap);
					max_flow+=flow;
					ans+=flow*dis[T];
					for (int i=T;i!=S;i=pre[i]->from)
					{
						pre[i]->cap-=flow;
						pre[i]->rev->cap+=flow;
					}
					return 1;
				}
			public:
				flow_graph (int _n,int _S,int _T)
				{
					n=_n;
					S=_S;
					T=_T;
					v=new node*[n+1]();
					dis=new type[n+1]();
					used=new int[n+1]();
					pre=new node*[n+1]();
					for (int i=1;i<=n;++i)
						v[i]=pre[i]=0;
				}
				void addedge(int x,int y,type c,type w)
				{
					node *p=new node;
					node *q=new node;
					*p=(node){x,y,c,w,v[x],q};
					*q=(node){y,x,0,-w,v[y],p};
					v[x]=p;
					v[y]=q;
				}
				pair<type,type> solve()
				{
					max_flow=ans=0;
					while (SPFA());
					return pair<type,type>(max_flow,ans);
				}
		};
	}
	
using namespace spfa_cost_flow;

const int INF=1000000000;

int n,m;
char s[110][110];
int l[110][110],r[110][110],u[110][110],d[110][110];

int place(int x,int y)
{
	return (x-1)*m+y;
}

int main()
{
	freopen("try.in","r",stdin);
	freopen("try.out","w",stdout);
	int Test;
	cin>>Test;
	for (int TT=1;TT<=100;++TT)
	{
		if (TT==29)
		{
			++TT;
			--TT;
		}
		printf("Case #%d: ",TT);
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;++i)
			scanf("%s",s[i]+1);
		for (int i=1;i<=n;++i)
		{
			l[i][0]=0;
			for (int j=1;j<=m;++j)
				l[i][j]=l[i][j-1]|(s[i][j]!='.');
			r[i][m+1]=0;
			for (int j=m;j>=1;--j)
				r[i][j]=r[i][j+1]|(s[i][j]!='.');
		}
		for (int j=1;j<=m;++j)
		{
			u[0][j]=0;
			for (int i=1;i<=n;++i)
				u[i][j]=u[i-1][j]|(s[i][j]!='.');
			d[n+1][j]=0;
			for (int i=n;i>=1;--i)
				d[i][j]=d[i+1][j]|(s[i][j]!='.');
		}
		int S=n*m+5,T=n*m+6;
		int lv=n*m+1,rv=n*m+2,uv=n*m+3,dv=n*m+4;
		spfa_cost_flow::flow_graph<int> G(n*m+6,S,T);
		G.addedge(S,lv,INF,0);
		G.addedge(S,rv,INF,0);
		G.addedge(S,uv,INF,0);
		G.addedge(S,dv,INF,0);
		int cnt=0;
		for (int i=1;i<=n;++i)
			for (int j=1;j<=m;++j)
				if (s[i][j]!='.')
				{
					if (l[i][j-1]&&r[i][j+1]&&u[i-1][j]&&d[i+1][j]) continue;
					++cnt;
					if (l[i][j-1]) G.addedge(lv,place(i,j),1,s[i][j]!='<');
					if (r[i][j+1]) G.addedge(rv,place(i,j),1,s[i][j]!='>');
					if (u[i-1][j]) G.addedge(uv,place(i,j),1,s[i][j]!='^');
					if (d[i+1][j]) G.addedge(dv,place(i,j),1,s[i][j]!='v');
					G.addedge(place(i,j),T,1,0);
				}
		pii ans=G.solve();
		if (ans.X!=cnt)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans.Y);
	}
	return 0;
}
