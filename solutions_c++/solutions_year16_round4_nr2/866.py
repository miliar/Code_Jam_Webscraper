#include <bits/stdc++.h>
#define openfile(s) freopen(s".in","r",stdin);freopen(s".out","w",stdout)
#define mpr std::make_pair
#define lg(x) (31-__builtin_clz(x))
#define lgll(x) (63-__builtin_clzll(x))
#define __count __builtin_popcount
#define __countll __builtin_popcountll
#define X first
#define Y second
#define mst(x) memset(x,0,sizeof(x))
#define mst1(x) memset(x,-1,sizeof(x))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define FORit(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define pb push_back
#define RI(x) scanf("%d",&x)
#define RID(x) int x;RI(x)
using namespace std;
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}
const int N=1010, INF=1e9;
const LD EPS=1e-7;
int T;
int n,k;
double pr[N];
int stop = 0;
int st[N];
int l;
double ans, best;
void dfsp(int i, int cn, double p){
	if(cn == l && i == k){
		ans += p;
		return;
	} else if(i == k){
		return;
	} else{
		dfsp(i+1, cn  , p* (1-pr[st[i]]) );	
		dfsp(i+1, cn+1, p* pr[st[i]]     );	
	}
}

void solve(){
	ans = 0;
	dfsp(0, 0, 1);
	if(ans > best){
		best = ans;
//FOR(i, k) printf("%d ", st[i]);puts("");	
	}
}
void dfs(int i, int n){
	if(stop == k){
		solve();
		return;
	} else if(i == n){
		return;
	} else {
		dfs(i+1, n);
		st[stop ++] = i;
		dfs(i+1, n);
		stop --;
	}
	return;
}

int main(){
	int t = 0;
	scanf("%d",&T);
	while(t++ < T){
		best = 0;
		RI(n); RI(k);
		FOR(i, n) scanf("%lf", &pr[i]);
		l = k/2;
		dfs(0, n);
		printf("Case #%d: ",t);	
		printf("%.10lf\n", best);
	}
}
