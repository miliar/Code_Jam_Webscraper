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

double a[1005],b[1005];

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/D-large.in","r",stdin);
	freopen("/Users/mac/Desktop/D.txt","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		int n;
		scanf("%d",&n);
		FOR(i,n) scanf("%lf",&a[i]);
		FOR(i,n) scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		int ans = 0,ans1 = 0;
		for(int i = 0;i<n;i++){
			int now = i;
			int ret = 0;
			for(int j = 0;j<n&&now<n;j++){
				if(a[now]>b[j]) ret++;
				now++;
			}
			ans = max(ans,ret);
		}
		multiset<double> s;
		for(int i = 0;i<n;i++) s.insert(b[i]);
		FOR(i,n){
			multiset<double>::iterator it = s.upper_bound(a[i]);
			if(it==s.end()){
				s.erase(s.begin());
				ans1++;
			}else{
				s.erase(it);
			}
		}
		static int ca = 1;
		cout<<"Case #"<<ca++<<": ";
		cout<<ans<<" "<<ans1<<endl;
	}
	return 0;
}

