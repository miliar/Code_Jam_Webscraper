/**
	site
	The.Repeater (Level: A)
	Source: GCJ.R1C 2014
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
	#define GETTIME		fprintf(stderr, "Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
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

char strs[100][110];
int stridx[100];
int len[100];

void solve_saving()
{
	int t = GI;
	REP(i, t)
	{
		memset(stridx, 0, sizeof(stridx));
		
		bool sol = true;
		bool finish = false;
		int n = GI;
		
		REP(j, n) 
		{
			cin >> strs[j];
			len[j] = strlen(strs[j]);
		}

		int counter[100] = {0};
		int __min = 0;
		
		while (sol && ! finish)
		{
			char match = strs[0][stridx[0]];
			SHOW( "matching " << match << endl );
			
			REP(j, n)
			{
				if (match != strs[j][stridx[j]])
				{
					sol = false;
					break;
				}
				
				counter[j] = 1;
				while (stridx[j]+1 < len[j] && strs[j][stridx[j]] == strs[j][stridx[j] + 1]) 
				{
					stridx[j]++;
					counter[j]++;
				}
				stridx[j]++;
				
				SHOW( "counter on " << j << ": " << counter[j]<< endl );
				SHOW( "index on " << j << ": " << stridx[j] << " of " << len[j] << endl );
			}
			if (sol)
			{
				int sum = 0;
				REP(j, n)
					sum += counter[j];
				int med = (int)((double)sum / n);
				SHOW( "med: " << med << endl );
				
				REP(j, n)
				{
					int dif = counter[j] - med;
					SHOW( "dif: " << dif << endl );
					__min += (dif < 0) ? -dif : dif;
				}
			}
			int f = 0;
			REP(j, n)
				if (stridx[j] >= len[j]) 
					f++;

			if (f > 0)
				if (f == n)
					finish = true;
				else
					sol = false;
		}

		cout << "Case #" << i+1 << ": ";
		if (sol)
			cout << __min << endl;
		else
			cout << "Fegla Won" << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
