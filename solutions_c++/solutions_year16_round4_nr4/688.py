#include <cstdio>
#include <vector>
#include <cstring>
#include <functional>
#include <algorithm>
#include <math.h>
#include <bitset>
#include <set>
#include <queue>
#include <assert.h>
#include <iostream>
#include <string>
#include <sstream>
#include <stack>
#include <complex>
#include <numeric>
#include <map>
#include <time.h>
using namespace std;
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int,int> pii;
typedef pair<int,ll> pil;
typedef pair<int,ull> piu;
typedef pair<ull,ull> puu;
typedef pair<ll,int> pli;
typedef pair<ll,ll> pll;
typedef pair<pii,ll> ppl;
typedef pair<ll,pii> plp;
typedef pair<ll,pll> plP;
typedef pair<int,pii> pip;
typedef pair<pii,int> ppi;
typedef pair<pii,pii> ppp;
typedef pair<double,int> pdi;
typedef pair<int,double> pid;
typedef pair<double,pii> pdp;
typedef pair<double,double> pdd;
typedef pair<pdd,double> pd3;
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
#define BS2(x,n,a) binary_search((x),(x)+(n),(a))
#define NB(x) (((x)&~((x)+((x)&-(x))))/((x)&-(x))>>1)|((x)+((x)&-(x)))
#define NP(x) next_permutation((x).begin(),(x).end())
#define MM(x,p) memset((x),(p),sizeof(x))
#define SQ(x) (x)*(x)
#define SC(c1,c2) strcmp(c1,c2)==0
#define mp make_pair
#define INF (1<<28)
#define INFL (1LL<<61)
#define fi first
#define se second
#define EPS 1e-9
#define MOD 1000000007
#define MIN(x,a) x=min(x,a)
#define MAX(x,a) x=max(x,a)
#define madd(x,a) x=(x+a)%MOD
#define msub(x,a) x=(x+MOD-a)%MOD
#define OUTPUT(x) rep(__,x.size())printf("%d%c",x[__],__+1==x.size()?'\n':' ');

int T;
int N;
char m[25][26];

struct UnionFind
{
	int par[25],sz[25],val[25];
	void init(){rep(i,25)par[i]=i,sz[i]=1,val[i]=0;}
	int find(int x){return par[x]==x?x:par[x]=find(par[x]);}
	bool same(int a,int b){return find(a)==find(b);}
	void unite(int a,int b)
	{
		if((a=find(a))!=(b=find(b)))
		{
			if(sz[a]<sz[b])swap(a,b);
			par[b]=a;
			sz[a]+=sz[b];
			val[a]+=val[b];
		}
	}
	void add(int a)
	{
		val[find(a)]++;
	}
}uf;
int btp[4];

int main()
{
	scanf("%d",&T);
	repn(_,1,T+1)
	{
		int res=111;
		scanf("%d",&N);
		rep(i,N)scanf("%s",&m[i]);
		int bt=0;
		rep(i,N)rep(j,N)bt+=(m[i][j]-'0')<<(i*N+j);
		rep(b,1<<(N*N))if((b&bt)==bt)
		{
			uf.init();
			bool ok=true;
			rep(j,N)
			{
				int las=-1;
				rep(i,N)if(b>>(i*N+j)&1)
				{
					if(las!=-1)uf.unite(i,las);
					las=i;
				}
			}
			rep(i,N)btp[i]=(b>>(N*i))%(1<<N);
			rep(i,N)if(btp[i]==0)ok=false;
			rep(i,N)ok&=(btp[i]==btp[uf.find(i)]);
			rep(i,N)if(uf.find(i)==i)
			{
				int p1=__builtin_popcount(btp[i]);
				int p2=uf.sz[i];
				if(p1!=p2)ok=false;
			}
			int kk=__builtin_popcount(b&~bt);
			if(ok)
			{
				MIN(res,kk);
				if(kk==2)
				{
					//rep(i,N)printf("%d %d %d\n",i,uf.find(i),btp[i]);
				}
			}
			//if(ok)printf("%d %d\n",res,kk);
		}
		printf("Case #%d: %d\n",_,res);
	}
}