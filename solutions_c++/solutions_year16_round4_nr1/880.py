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
int N,G,C,P;
vector<string> g,c,p;

int main()
{
	scanf("%d",&T);
	repn(__,1,T+1)
	{
		scanf("%d%d%d%d",&N,&G,&P,&C);
		g.clear();c.clear();p.clear();
		rep(i,G)g.pb("R");
		rep(i,C)c.pb("S");
		rep(i,P)p.pb("P");
		bool bad=false;
		rep(i,N)
		{
			int gn=g.size();
			int cn=c.size();
			int pn=p.size();
			if(gn>cn+pn||cn>gn+pn||pn>gn+cn)
			{
				bad=true;
				break;
			}
			int cp=(cn+pn-gn)/2;
			int gc=cn-cp;
			int gp=pn-cp;
			if(cp<0||gp<0||gc<0)
			{
				bad=true;
				break;
			}
			vector<string> ng,nc,np;
			int gptr=0,cptr=0,pptr=0;
			rep(j,cp)nc.pb(min(c[cptr]+p[pptr],p[pptr]+c[cptr])),pptr++,cptr++;
			rep(j,gc)ng.pb(min(c[cptr]+g[gptr],g[gptr]+c[cptr])),gptr++,cptr++;
			rep(i,gp)np.pb(min(g[gptr]+p[pptr],p[pptr]+g[gptr])),pptr++,gptr++;
			c=nc,g=ng,p=np;
		}
		printf("Case #%d: ",__);
		if(bad)puts("IMPOSSIBLE");
		else
		{
			if(g.size())cout<<g[0]<<endl;
			if(c.size())cout<<c[0]<<endl;
			if(p.size())cout<<p[0]<<endl;
		}
	}
}