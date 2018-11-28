/**
	site
	4 name (Code: deceitful.war)
	Source: GCJ.Qualification.Round 2014
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <iterator>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>

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

#define DEBUG

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

const int _max = 1000;

int naomi[_max] = {0};
int naomi2[_max] = {0};
int ken[_max] = {0};
int ken2[_max] = {0};

void solve_saving()
{
	int t = GI;
	REP(i, t)
	{
		int n = GI;
		REP(j, n)
		{
			double real = GD;
			naomi[j] = ((int)(real * 1000000)) / 10;
		}
		REP(j, n)
		{
			double real = GD;
			ken[j] = ((int)(real * 1000000)) / 10;
		}

		sort(naomi, naomi + n);
		sort(ken, ken + n);
		
		memcpy(naomi2, naomi, sizeof(int) * n);
		memcpy(ken2, ken, sizeof(int) * n);
		
		int war = 0;
		int deceitful = 0;
		
		int begin = 0;
		int end = n-1;
		int kbegin = 0;
		
		REP(j, n)	
		{
			// playing War (Naomi send biggest block avail, Ken select next bigger block or the smallest one if he gonna loss anyway)
			int* iterator = find_if(ken, ken + n, bind2nd(greater<int>(), naomi[n - j - 1]));
			if (iterator == ken + n)
			{
				war++;
				ken[kbegin] = -1;
			}
			else
				*iterator = -1;
			while (kbegin < n && ken[kbegin] == -1) kbegin++;
			
			// playing Deceitful War (Naomi force ken to send smallest and she send smaller block higher that his)
			int * it = find_if(naomi2, naomi2 + n, bind2nd(greater<int>(), ken2[j]));
			if (it == naomi2 + n)
			{
				naomi2[begin] = -1;	// and all remaining will loss too
			}
			else
			{
				deceitful++;
				*it = -1;
			}
			while (begin < n && naomi2[begin] == -1) begin++;
		}
		cout << "Case #" << i+1 << ": " << deceitful << " " << war << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
