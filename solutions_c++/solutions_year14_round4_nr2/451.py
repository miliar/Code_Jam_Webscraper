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

int T,N;
int A[1000];
pii P[1000];

struct BIT
{
	int bit[2048];
	void init(){MM(bit,0);}
	void add(int x,int v){x++;while(x<2048)bit[x]+=v,x+=x&-x;}
	int sum(int x){x++;int r=0;while(x>0)r+=bit[x],x-=x&-x;return r;}
} bit1,bit2;

int main()
{
	scanf("%d",&T);
	repn(__,1,T+1)
	{
		scanf("%d",&N);
		rep(i,N)scanf("%d",&A[i]);
		vector<int> xx;
		rep(i,N)xx.pb(A[i]);
		SORT(xx);ERASE(xx);
		rep(i,N)A[i]=LB(xx,A[i]);
		rep(i,N)P[i]=mp(A[i],i);
		sort(P,P+N);
		bit1.init(),bit2.init();
		int sz=N;
		rep(i,N)bit1.add(i,1);
		int ans=0;
		rep(i,N)
		{
			int lf=bit1.sum(P[i].se-1),rf=sz-bit1.sum(P[i].se);
			ans+=min(lf,rf);
			bit1.add(P[i].se,-1);
			sz--;
		}
		printf("Case #%d: %d\n",__,ans);
	}
}
