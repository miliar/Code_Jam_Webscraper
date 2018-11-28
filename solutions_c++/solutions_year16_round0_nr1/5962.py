/**
	site
	A name (Code: Counting_Sheep)
	Source: GCJ 2016
*/

#include <cstdio>
#include <cstdlib>

#include <iostream>

typedef long long unsigned llu;

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})

#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define REP(i,n) FOR(i,0,n)

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

bool digits[10];
int d;

inline void process(llu n)
{
  while (n)
  {
    SHOW("\t" << n << endl);
    
    int a = n % 10;
    n /= 10;
    if (! digits[a])
    {
      d++;
      digits[a] = true;
    }
  }
}

void solve_saving()
{
	int t = GI;
	REP(i, t)
	{
		llu n; n = GL;
		if (n == 0)
		{
		  printf("Case #%d: INSOMNIA\n", i+1);
		  continue;
		}
		
		memset(digits, 0, sizeof(digits));
		d = 0;
		
		int j = 1;
		while (d < 10)
		{
		  SHOW(d << " " << n*j << endl);
		
		  process(n * j);
		  j++;
		}
		printf("Case #%d: %llu\n", i+1, n*(j-1));
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
