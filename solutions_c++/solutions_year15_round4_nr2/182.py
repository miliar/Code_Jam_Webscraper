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

struct Item{
	long double R,X;
	bool operator<(const Item &it) const{
		return X<it.X;
	}
} it[105];

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/data.in","r",stdin);
	freopen("/Users/mac/Desktop/data.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		int n;
		long double v,x;
		scanf("%d %Lf %Lf",&n,&v,&x);
		FOR(i,n) scanf("%Lf %Lf",&it[i].R,&it[i].X);
		sort(it,it+n);
		long double low = 0,high = 1e10;
		while(low+1e-11<high){
			long double mid = (low+high)/2;
			long double sum = 0;
			FOR(i,n) sum+=it[i].R;
			long double need = v,tot = 0;
			long double mi = 0,mx = 0;
			FOR(i,n){
				if(need==0) break;
				long double use = min(need,it[i].R*mid);
				tot+=use*it[i].X;
				need-=use;
			}
			mi = tot;
			need = v,tot = 0;
			for(int i = n-1;i>=0;i--){
				if(need==0) break;
				long double use = min(need,it[i].R*mid);
				tot+=use*it[i].X;
				need-=use;
			}
			mx = tot;
			if(mid>=v/sum&&mi<=x*v&&x*v<=mx){
				high = mid;
			}else low = mid;
		}
		static int ca = 1;
		printf("Case #%d: ",ca++);
		if(low>1e9) puts("IMPOSSIBLE");
		else printf("%.10Lf\n",low);
	}
	return 0;
}

