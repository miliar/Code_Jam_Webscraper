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

int n,num;
const int prime[] = {3,5,7,11,13,17,19};
int val[35];
int ret[35];

void dfs(int cur){
	if(cur==0){
		int ok = 1;
		for(int b = 2;b<=10;b++){
			int find = 0;
			for(int j = 0;j<7;j++){
				int md = 0;
				int now = 1;
				int p = prime[j];
				for(int i = 0;i<n;i++){
					if(val[i]){
						md+=now%p;
						md%=p;
					}
					now = now*b%p;
				}
				if(md==0){
					ret[b] = p;
					find = 1;
					break;
				}
			}
			if(!find) ok = 0;
		}
		if(ok){
			for(int i = n-1;i>=0;i--) printf("%d",val[i]);
			putchar(' ');
			for(int i = 2;i<=10;i++) printf("%d ",ret[i]);
			puts("");
			if(--num==0){
				exit(0);
			}
		}
		return;
	}
	val[cur] = 0;
	dfs(cur-1);
	val[cur] = 1;
	dfs(cur-1);
}

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/data.in","r",stdin);
	freopen("/Users/mac/Desktop/data.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&num);
		puts("Case #1:");
		val[0] = val[n-1] = 1;
		dfs(n-2);
	}
	return 0;
}

