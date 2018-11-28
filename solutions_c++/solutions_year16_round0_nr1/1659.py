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

LL ans[MAXN];

int state(LL val){
	int ans = 0;
	while(val){
		ans|=(1<<(val%10));
		val/=10;
	}
	return ans;
}

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/data.in","r",stdin);
	freopen("/Users/mac/Desktop/data.out","w",stdout);
#endif
	for(int i = 1;i<MAXN;i++){
		int st = 0;
		for(LL j = 1;;j++){
			st|=state(j*i);
			if(st==(1<<10)-1){
				ans[i] = j*i;
				break;
			}
		}
	}
	int t;
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d",&n);
		static int ca = 1;
		if(n==0){
			printf("Case #%d: INSOMNIA\n",ca++);
		}else
			printf("Case #%d: %lld\n",ca++,ans[n]);
	}
	return 0;
}

