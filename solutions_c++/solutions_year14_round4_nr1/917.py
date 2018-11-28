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

int a[10005];

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/A.in","r",stdin);
	freopen("/Users/mac/Desktop/A.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		int n,x;
		cin>>n>>x;
		for(int i = 0;i<n;i++) cin>>a[i];
		sort(a,a+n);
		int i = 0,j = n-1;
		int ans = 0;
		while(i<=j){
			if(i==j){
				ans++;
				break;
			}
			while(i<j&&a[i]+a[j]>x){
				j--;
				ans++;
			}
			ans++;
			i++,j--;
		}
		static int ca = 1;
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}

