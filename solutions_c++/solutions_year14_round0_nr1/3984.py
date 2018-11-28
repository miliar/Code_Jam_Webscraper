/**
	site
	1 name (Code: magic.trick)
	Source: GCJ 2014
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


void solve_saving()
{
	int t = GI;
	REP(i, t)
	{
		int m1[4][4] = {0};
		int m2[4][4] = {0};
		
		int row1 = GI;
		REP(j, 4)
			REP(k, 4)
				m1[j][k] = GI;
		int row2 = GI;
		REP(j, 4)
			REP(k, 4)
				m2[j][k] = GI;
				
		int solcount = 0;
		int sol = 0;
		REP(j, 4)	// through row in m1
			REP(k, 4)	// through row in m2
				if (m1[row1-1][j] == m2[row2-1][k]) 
				{
					solcount++;
					sol = m1[row1-1][j];
// 					SHOW( "case " << i+1 << " " << solcount << " " << sol << endl );
				}
		
		cout << "Case #" << i+1 << ": ";
		if (solcount == 0)
			cout << "Volunteer cheated!" << endl;
		else if (solcount == 1)
			cout << sol << endl;
		else
			cout << "Bad magician!" << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
