#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <numeric>
#include <tuple>
#include <climits>

#define INF 1023456789
#define SQR(x) ((x)*(x))
#define INIT(x,y) memset((x),(y),sizeof((x)))
#define SIZE(x) ((int)((x).size()))
#define REP(i, n) for (__typeof(n) i=0;i<(n);++i)
#define FOR(i, a, b) for (__typeof(a) i=(a);i<=(b);++i)
#define FORD(i, a, b) for (__typeof(a) i=(a);i>=(b);--i)
#define FORE(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

#define DEBUG
#ifdef DEBUG
#define DBG(x) cerr << #x << ": " << (x) << endl;
#else
#define DBG(x)
#endif

using namespace std;
 
typedef long long LL;
typedef pair<int,int> PI;
typedef tuple<int,int,int>trio;

int N;
double a[1047],b[1047];

inline int first()
{
	int j = N-1, i = 0;
	while (b[j]>a[N-1]) j--,i++;
	a[N] = 2;
	int found = 0;
	REP(pos,j+1) 
	{
		while (a[i]<b[pos]) ++i;
		if (b[pos]<a[i] && i!=N) found++;
		if (i==N) break;
		i++;
	}
	return found;
}

inline int second()
{
	int pos = 0;
	b[N] = 2;
	int found = 0;
	REP(i,N)
	{
		while (b[pos]<a[i]) 
		{
			pos++; 
		}
		if (a[i]<b[pos] && pos!=N) found++;
		if (pos==N) break;
		pos++;
	}
	return N-found;
}

inline void solve(int test)
{
	scanf("%d",&N);
	REP(i,N) scanf("%lf",&a[i]);
	REP(i,N) scanf("%lf",&b[i]);
	sort(a,a+N);
	sort(b,b+N);
	printf("Case #%d: %d %d\n",test,first(),second());
}

int main()
{
	int T;
	scanf("%d",&T);
	REP(i,T) solve(i+1);
        return 0;
}
