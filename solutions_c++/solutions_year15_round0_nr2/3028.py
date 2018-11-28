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

void solve(int t)
{
	int D;
	cin >> D;
	int p[1047];
	int worst = 0;
	REP(i,D) 
	{
		cin >> p[i];
		worst = max(worst,p[i]);
	}
	int result = worst;
	FORD(i,worst-1,1) 
	{
		int current = i;
		REP(j,D) current += (p[j]-1)  / i; 
		result = min(result, current);
	}
	cout << "Case #" << t << ": " << result << endl;
}

int main()
{
	int T;
	cin >> T;
	REP(i,T) solve(i+1);
        return 0;
}
