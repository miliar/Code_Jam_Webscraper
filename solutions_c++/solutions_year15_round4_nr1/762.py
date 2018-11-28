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
typedef pair<ll,int> pli;
typedef pair<ll,ll> pll;
typedef pair<pii,ll> ppl;
typedef pair<ll,pii> plp;
typedef pair<int,pii> pip;
typedef pair<pii,int> ppi;
typedef pair<pii,pii> ppp;
typedef pair<double,int> pdi;
typedef pair<int,double> pid;
typedef pair<double,pii> pdp;
typedef pair<double,double> pdd;
typedef pair<pdd,double> pd3;
typedef vector<int> vec;
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
#define MOD 1000000007
#define EPS 1e-12
#define MIN(x,a) x=min(x,a)
#define MAX(x,a) x=max(x,a)
#define madd(x,a) x=(x+a)%MOD
#define msub(x,a) x=(x+MOD-a)%MOD
#define OUTPUT(x) rep(i,x.size())printf("%d%c",x[i],i+1==x.size()?'\n':' ');

int T,H,W;
char m[100][101];
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
bool can[4];

int main()
{
	scanf("%d",&T);
	repn(_,1,T+1)
	{
		printf("Case #%d: ",_);
		scanf("%d%d",&H,&W);
		rep(i,H)scanf("%s",&m[i]);
		int res=0;
		rep(i,H)rep(j,W)if(m[i][j]!='.')
		{
			can[0]=can[1]=can[2]=can[3]=false;
			rep(dd,4)
			{
				int x=i+dx[dd],y=j+dy[dd];
				while(0<=x&&x<H&&0<=y&&y<W&&m[x][y]=='.')x+=dx[dd],y+=dy[dd];
				can[dd]=(0<=x&&x<H&&0<=y&&y<W);
			}
			if(can[0]==false&&can[1]==false&&can[2]==false&&can[3]==false)res=-114514;
			else if(m[i][j]=='v'&&can[0]);
			else if(m[i][j]=='^'&&can[1]);
			else if(m[i][j]=='>'&&can[2]);
			else if(m[i][j]=='<'&&can[3]);
			else res++;
		}
		if(res<0)puts("IMPOSSIBLE");
		else printf("%d\n",res);
	}
}