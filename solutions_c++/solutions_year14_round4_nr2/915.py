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
const int INF = 0x3fffffff;
const LL LINF = INF * 1ll * INF;
const double PI = acos(-1.0);

#define lson l,mid,rt<<1
#define rson mid+1,r,rt<<1|1
#define lowbit(u) (u&(-u))

using namespace std;

LL dp[1005][1005];
int x[1005];
int a[1005];
PII p[1005];
LL tot1[1005],tot2[1005];
int n;

LL dfs(int i,int j){
	if(~dp[i][j]) return dp[i][j];
	int nxt = i+j;
	if(nxt==n) return 0;
	dp[i][j] = LINF;
	dp[i][j] = min(dfs(i+1,j)+tot1[p[nxt].second],
			dfs(i,j+1)+tot2[p[nxt].second]);
	return dp[i][j];
}

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/B-large.in","r",stdin);
	freopen("/Users/mac/Desktop/B1.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		memset(tot1,0,sizeof(tot1));
		memset(tot2,0,sizeof(tot2));
		for(int i = 0;i<n;i++){
			scanf("%d",&a[i]);
			p[i] = MP(a[i],i);
			for(int j = 0;j<i;j++) if(a[j]>a[i]) tot1[i]++;
		}
		for(int i = 0;i<n;i++){
			for(int j = i+1;j<n;j++) if(a[j]>a[i]) tot2[i]++;
		}
		sort(p,p+n);
		memset(dp,-1,sizeof(dp));
		LL ans = dfs(0,0);
		static int ca = 1;
		printf("Case #%d: %lld\n",ca++,ans);
	}
	return 0;
}

