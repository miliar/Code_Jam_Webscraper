//#pragma comment(linker,"/STACK:102400000,102400000")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <ctime>
#include <numeric>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <complex>
#include <deque>
#include <functional>
#include <list>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
using namespace std;
template<class T> inline T sqr(T x) { return x * x; }
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int, int> PII;
typedef pair<PII, int> PIII;
typedef pair<LL, LL> PLL;
typedef pair<LL, int> PLI;
typedef pair<LD, LD> PDD;
#define MP make_pair
#define PB push_back
#define sz(x) ((int)(x).size())
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define istr stringstream
#define FOR(i,n) for(int i=0;i<(n);++i)
#define forIt(mp,it) for(__typeof(mp.begin()) it = mp.begin();it!=mp.end();it++)
const double EPS = 1e-6;
const int INF = 0x3fffffff;
const LL LINF = INF * 1ll * INF;
const double PI = acos(-1.0);

#define lson l,mid,rt<<1
#define rson mid+1,r,rt<<1|1
#define lowbit(u) (u&(-u))

using namespace std;

#define MAXN 1000005

int s[MAXN],m[MAXN];
vector<int> g[MAXN];
vector<int> v[MAXN];
int flag[MAXN];
int sz[MAXN],fa[MAXN];

int find(int u){
	return fa[u]==u?u:fa[u] = find(fa[u]);
}

void Add(int u){
	if(flag[u]==-1) return;
	flag[u] = 1;
	int sz = g[u].size();
	FOR(j,sz){
		int v = g[u][j];
		int fv = find(v),fu = find(u);
		if(fv==fu||flag[v]!=1) continue;
		fa[fv] = fu;
		::sz[fu]+=::sz[fv];
	}
	if(u==0) return;
	int f = m[u]%u;
	int fv = find(f),fu = find(u);
	if(fv!=fu&&flag[f]==1){
		fa[fv] = fu;
		::sz[fu]+=::sz[fv];
	}
}

void Remove(int u){
	if(flag[u]==-1) return;
	sz[find(u)]--;
	flag[u] = -1;
	int sz = g[u].size();
	FOR(i,sz){
		int v = g[u][i];
		Remove(v);
	}
}

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/data.in","r",stdin);
	freopen("/Users/mac/Desktop/data.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		int n,d;
		scanf("%d %d",&n,&d);
		int as,cs,rs;
		scanf("%d %d %d %d",&s[0],&as,&cs,&rs);
		FOR(i,rs) v[i].clear();
		for(int i = 0;i<n-1;i++) s[i+1] = (1ll*s[i]*as+cs)%rs;
		FOR(i,n) v[s[i]].PB(i);
		int am,cm,rm;
		scanf("%d %d %d %d",&m[0],&am,&cm,&rm);
		FOR(i,n) g[i].clear();
		for(int i = 0;i<n-1;i++) m[i+1] = (1ll*m[i]*am+cm)%rm;
		for(int i = 1;i<n;i++){
			g[m[i]%i].PB(i);
		}
		FOR(i,n) flag[i] = 0;
		FOR(i,n) fa[i] = i,sz[i] = 1;
		int ans = 0;
		FOR(i,rs){
			int sz = v[i].size();
			FOR(j,sz){
				int u = v[i][j];
				Add(u);
			}
			ans = max(ans,::sz[find(0)]);
			if(i>=d){
				sz = v[i-d].size();
				FOR(j,sz){
					int x = v[i-d][j];
					Remove(x);
				}
			}
		}
		static int ca = 1;
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}

