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
const double PI = acos(-1.0);

#define lson l,mid,rt<<1
#define rson mid+1,r,rt<<1|1
#define lowbit(u) (u&(-u))

using namespace std;

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/B.in","r",stdin);
	freopen("/Users/mac/Desktop/B.txt","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		static int ca = 1;
		printf("Case #%d: ",ca++);
		if(c>=x){
			printf("%.10lf\n",x/2);
			continue;
		}
		double ans = x/2;
		double speed = 2;
		double now = 0;
		double cost = 0;
		while(true){
			double tmp = (c-now)/speed;
			if(x/(speed+f)+cost+tmp<ans){
				ans = x/(speed+f)+cost+tmp;
				now = 0;
				speed+=f;
				cost+=tmp;
			}else break;
		}
		printf("%.10f\n",ans);
	}
	return 0;
}

