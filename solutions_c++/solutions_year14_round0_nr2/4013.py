/**
	site
	2 name (Code: cookie.clicker.alpha)
	Source: GCJ.Qualification.Round 2014
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
		double C = GD;
		double F = GD;
		double X = GD;
		
		double timespend= 0.0;
		double cookierate = 2.0;
		
		double produce, buy, nextproduce;
		bool solved = false;
		while (! solved) 
		{
			produce = X / cookierate;
			buy = C / cookierate;
			nextproduce = X / (cookierate + F);
		
			if (produce < buy + nextproduce)
				solved = true;
			else
			{
				cookierate += F;
				timespend += buy;
			}
		}
		printf("Case #%d: %.7lf\n", i+1, timespend + produce);
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
