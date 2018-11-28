//author - techaddict
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <climits>
#include <cassert>
using namespace std;

#define S(n) scanf("%d",&n)
#define P(n) printf("%d ",n)
#define SL(n) scanf("%lld",&n)
#define PL(n) printf("%lld ",n)
#define SF(n) scanf("%lf",&n)
#define PF(n) printf("%lf ",n)
#define SS(n) scanf("%s",n)
#define INF INT_MAX
#define LINF (long long int)1e18
#define EPS 1e-11
const double PI=acos(-1.0);
#define two(X) (1<<x)
#define twoL(X) (((LL)(1))<<(X))
#define contain(S,X) (((S)&two(x))!=0)
#define containL(S,X) (((S)&twoL(x))!=0)
#define maX(a,b) ((a)>(b)?(a):(b))
#define miN(a,b) ((a)<(b)?(a):(b))
#define abs(a) ((a)<0?-(a):(a))
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define foreach(v,c) for(typeof((c).begin()) v=(c).begin(); v!=(c).end(); ++v)
#define MP make_pair
#define FR first
#define SE second
#define tri(a,b,c) MP(a,MP(b,c))
#define fill(a,v) memset(a,v,sizeof a)
#define cpy(b,a) memcpy(b,a,sizeof a)
#define ALL(c) (c).begin(), (c).end() 
#define SZ(v) ((int)(v.size()))
#define DREP(a) sort(ALL(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
#define PB(X) push_back(X)
#define dump(x)  cerr << #x << " = " << (x) << endl

#ifndef ONLINE_JUDGE
#define DEBUG
#endif

#ifdef DEBUG
#define cvar(x) cerr << "<" << #x << ": " << x << ">"
#define evar(x) cvar (x) << endl
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
#else
#define cvar(...) ({})
#define evar(...) ({})
template<class T> void debug(T a,T b){}
#endif

typedef long long LL;
typedef unsigned long long int uint64;
typedef unsigned long int uint32;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<int, PII> TRI;

typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;

typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;

inline LL power(LL a,LL b,LL m){LL _r=1;while(b){if(b%2==1)_r=(_r*a)%m;a=(a*a)%m;b>>1;}return _r;} //a^b%m

//Main code starts
LL a[]={1L,
4L,
9L,
121L,
484L,
10201L,
12321L,
14641L,
40804L,
44944L,
1002001L,
1234321L,
4008004L,
100020001L,
102030201L,
104060401L,
121242121L,
123454321L,
125686521L,
400080004L,
404090404L,
10000200001L,
10221412201L,
12102420121L,
12345654321L,
40000800004L,
1000002000001L,
1002003002001L,
1004006004001L,
1020304030201L,
1022325232201L,
1024348434201L,
1210024200121L,
1212225222121L,
1214428244121L,
1232346432321L,
1234567654321L,
4000008000004L,
4004009004004L};
int main(){
	//ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	#endif
	int tests,n;
	LL s,e;
	S(tests);
	for(int test=1;test<=tests;test++){
		scanf("%lld%lld",&s,&e);
		int cnt=0;
		for(int i=0;i<39;i++){
			if(a[i]<=e&&a[i]>=s)cnt++;
		}
		printf("Case #%d: %d\n",test,cnt);
	}
}