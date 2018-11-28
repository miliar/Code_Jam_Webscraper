#include <cstdio>
#include <vector>
#include <cstring>
#include <functional>
#include <algorithm>
#include <math.h>
#include <bitset>
#include <set>
#include <queue>
#include <iostream>
#include <string>
#include <sstream>
#include <stack>
#include <complex>
#include <numeric>
#include <map>
#include <time.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<int,ll> pil;
typedef pair<ll,int> pli;
typedef pair<int,pii> pip;
typedef pair<pii,int> ppi;
typedef pair<ll,ll> pll;
typedef pair<double,int> pdi;
typedef pair<double,double> pdd;
typedef vector<double> vec;
typedef vector<vec> mat;
#define rep(i,n) for (int (i) = 0; (i) < (n); (i)++)
#define repn(i,a,n) for (int (i) = (a); (i) < (n); (i)++)
#define ALL(x) (x).begin(),(x).end()
#define pb push_back
#define SORT(x) sort((x).begin(),(x).end())
#define SORTN(x,n) sort((x),(x)+(n))
#define ERASE(x) (x).erase(unique((x).begin(),(x).end()),(x).end())
#define COUNT(x,c) count((x).begin(),(x).end(),(c))
#define REMOVE(x,c) (x).erase(remove((x).begin(),(x).end(),(c)),(x).end())
#define REVERSE(x) reverse((x).begin(),(x).end())
#define FORIT(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define LB(x,a) lower_bound((x).begin(),(x).end(),(a))-(x).begin()
#define lb(x,a) lower_bound((x).begin(),(x).end(),(a))
#define LBN(x,a,n) lower_bound((x),(x)+(n),(a))-(x)
#define lbN(x,a,n) lower_bound((x),(x)+(n),(a))
#define UB(x,a) upper_bound((x).begin(),(x).end(),(a))-(x).begin()
#define ub(x,a) upper_bound((x).begin(),(x).end(),(a))
#define BS(x,a) binary_search((x).begin(),(x).end(),(a))
#define NB(x) (((x)&~((x)+((x)&-(x))))/((x)&-(x))>>1)|((x)+((x)&-(x)))
#define NP(x) next_permutation((x).begin(),(x).end())
#define MM(x,p) memset((x),(p),sizeof(x))
#define SQ(x) (x)*(x)
#define SC(c1,c2) strcmp(c1,c2)==0
#define mp make_pair
#define INF (1<<30)
#define INFL (1LL<<56)
#define fi first
#define se second
#define MOD 1000000007
#define EPS 1e-9

#define MAX_V 1050000
struct edge{int to,cap,rev;};
vector<edge> G[MAX_V];
bool used[MAX_V];

void add_edge(int from,int to,int cap)
{
	G[from].push_back((edge){to,cap,G[to].size()});
	G[to].push_back((edge){from,0,G[from].size()-1});
}

int dfs(int v,int t,int f)
{
	if (v==t) return f;
	used[v] = true;
	for (int i = 0; i < G[v].size(); i++)
	{
		edge &e = G[v][i];
		if (!used[e.to]&&e.cap>0)
		{
			int d = dfs(e.to,t,min(f,e.cap));
			if (d>0)
			{
				e.cap-=d;
				G[e.to][e.rev].cap+=d;
				return d;
			}
		}
	}
	return 0;
}

int max_flow(int s,int t)
{
	int flow = 0;
	for (;;)
	{
		memset(used,0,sizeof(used));
		int f = dfs(s,t,INF);
		if (f==0) return flow;
		flow+=f;
	}
}

int T,W,H,B;
int X0[1000],Y0[1000],X1[1000],Y1[1000];
int gl[1010][1010];
int dx[4]={1,-1,0,0},dy[4]={0,0,1,-1};


int getgl(int a,int b){return (a>=0&&b>=0)?gl[a][b]:0;}
int main()
{
	scanf("%d",&T);
	repn(__,1,T+1)
	{
		rep(i,MAX_V)G[i].clear();
		scanf("%d%d%d",&W,&H,&B);
		vector<int> x,y;
		rep(i,B)
		{
			scanf("%d%d%d%d",&X0[i],&Y0[i],&X1[i],&Y1[i]);X1[i]++,Y1[i]++;
			y.pb(Y0[i]),y.pb(Y1[i]);
		}
		SORT(y);ERASE(y);
		//H=y.size();
		//rep(i,B)Y0[i]=LB(y,Y0[i]),Y1[i]=LB(y,Y1[i]);
		MM(gl,0);
		rep(i,B)gl[X0[i]][Y0[i]]++,gl[X0[i]][Y1[i]]--,gl[X1[i]][Y0[i]]--,gl[X1[i]][Y1[i]]++;
		rep(i,W)rep(j,H)gl[i][j]+=getgl(i-1,j)+getgl(i,j-1)-getgl(i-1,j-1);
		rep(i,W)rep(j,H)if(gl[i][j]==0)
		{
			rep(dd,4)
			{
				int nx=i+dx[dd],ny=j+dy[dd];
				if(0<=nx&&nx<W&&0<=ny&&ny<H&&gl[nx][ny]==0)
				{
					add_edge(i*H+j+250000,nx*H+ny,1);
				}
			}
		}
		rep(i,W)rep(j,H)add_edge(i*H+j,i*H+j+250000,1);
		int s=1000050,t=1000060;
		rep(i,W)if(gl[i][0]==0)add_edge(s,i*H,1);
		rep(i,W)if(gl[i][H-1]==0)add_edge(i*H+H-1+250000,t,1);
		printf("Case #%d: %d\n",__,max_flow(s,t));
	}
}
