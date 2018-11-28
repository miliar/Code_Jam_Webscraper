/**
	site
	C name (Code: Fair_and_Square)
	Source: GCJ 2013
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <iterator>
#include <algorithm>
#include <functional>
#include <string>
#include <map>
#include <vector>
#include <set>

typedef long long ll;
typedef long long unsigned llu;

#define	_min(a,b)	((a)<(b)?(a):(b))
#define _max(a,b)	((a)>(b)?(a):(b))

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define REP(i,n) FOR(i,0,n)

#define MOD 1000000007
#define INF (int)1e9
#define EPS 1e-9

#define IT(a,it) for (typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define pb push_back
#define mp make_pair

// #define DEBUG

#ifdef DEBUG
	std::string tabs;
	#define INDENT		tabs+="\t"
	#define _EXIT(val)	{ UNINDENT; return val; }
	#define UNINDENT	tabs.erase(tabs.length()-1)
	#define SHOW(x)		cout << tabs << x
	#include <time.h>
	#define STARTTIME	clock_t start = clock();
	#define GETTIME		printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
	#define _DEBUG(x)	x
#else
	#define INDENT
	#define _EXIT(val)	return val
	#define UNINDENT
	#define SHOW(x)
	#define STARTTIME
	#define GETTIME
	#define _DEBUG(x)
#endif

using namespace std;

const int pairs = 10000;

llu dp[10000001] = {0};	// solution for small and large case (10^14)
llu low[pairs], high[pairs];
llu lowest, highest;

bool ispal(llu n)
{
	// stringizing
	int str[20];
	int idx = 19;
	while (n)
	{
		str[idx--] = n % 10;
		n /= 10;
	}
	
	int limit = (idx+1 + 19) / 2;
	for (int i = idx, j = 20, inc = 1; i+inc <= limit; inc++)
	{
		if (str[i+inc] != str[j-inc])
			return false;
	}

	return true;
}

void solve_saving()
{
	lowest = 100000000000001L;
	highest = 0;
	
	int t = GI;
	REP(i, t)
	{
		cin >> low[i] >> high[i];
		lowest = _min(lowest, low[i]);
		highest = _max(highest, high[i]);
	}
	SHOW( "lowest: " << lowest << " highest: " << highest << endl );
	
	int low_sqrt = sqrt(lowest);
	if (low_sqrt * low_sqrt < lowest)
		low_sqrt++;
	int high_sqrt = sqrt(highest);
	if (high_sqrt * high_sqrt > highest)
		high_sqrt--;
	
	SHOW( "low_sqrt: " << low_sqrt << " high_sqrt: " << high_sqrt << endl );
	
	FOR(i, low_sqrt, high_sqrt+1)
	{
		if (ispal(i) && ispal(i*i))
		{
			dp[i] = dp[i-1]+1;
			SHOW(i << " " << i*i << endl);
		}
		else
			dp[i] = dp[i-1];
	}
	
	REP(i, t)
	{
		low_sqrt = sqrt(low[i]);
		if (low_sqrt * low_sqrt < low[i])
			low_sqrt++;
		high_sqrt = sqrt(high[i]);
		if (high_sqrt * high_sqrt > high[i])
			high_sqrt--;
		cout << "Case #" << i+1 << ": " << dp[high_sqrt] - dp[low_sqrt-1] << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
