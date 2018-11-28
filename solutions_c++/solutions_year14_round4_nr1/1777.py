// directives 
	#include <stdio.h>
	#include <vector>
	#include <map>
	#include <set>
	#include <deque>
	#include <queue>
	#include <algorithm>
	#include <iostream>
	#include <cmath>
	#include <cstring>
	#include <typeinfo>
	#include <sstream>
// 
using namespace std;
// macros 
	#define FOR(i,a,b)      for(int i(a);i<b;++i)
	#define REP(i,n)        FOR(i,0,n)
	#define FORD(i,a,b)      for(int i(a-1);i>=b;--i)
	#define CL(a,x)         memset(a,x,sizeof(a))
	#define FL(a,x)			fill_n(a,sizeof(a)/sizeof(a[0]),x)
	#define asort(a,n)		sort(a,a+n)
	#define vsort(v,n)		sort(v.begin(), v.begin()+n)
	#define sz(x)			x.size()
	#define all(x)			x.begin(), x.end()
	#define SSTR( x )		dynamic_cast< std::ostringstream & >( ( std::ostringstream() << std::dec << x ) ).str()
// 

typedef long long LL;
typedef vector<int> vi;
int rint() { int x; if(scanf("%d",&x)!=1) return -1; return x; }
LL rLL() { LL x; if(scanf("%lld",&x)!=1) return -1; return x; }
string rstring() { static char buf[100000]; if(scanf("%s",buf)!=1) return ""; return buf; }

int a[10005];
bool vis[10005];
int solve (int x, int n)
{
	CL(vis,false);
	int i = 0, j = n-1, c = 0;
	while (i < j) {
		if (vis[i]) {
			i++; continue;
		}
		vis[i] = true;
		while (j > i && a[j] > x-a[i]) j--;
		if (j != i) {
			vis[j--] = true;
		}
		c++;
	}
	REP(i,n) if (!vis[i]) c++;
	return c;
}

int main()
{
	int T = rint();
	REP(t, T) {
		int n = rint(), x = rint();
		REP(i,n) a[i] = rint();
		sort(a,a+n);
		printf("Case #%d: %d\n", t+1, solve(x,n));
	}
	return 0;
}
