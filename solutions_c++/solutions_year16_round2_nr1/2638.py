/**
	site
	A name (Code: Generating_the_digits)
	Source: GCJ.R1B 2016
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

typedef set< pair<char, int> > ci_pair;

typedef map<char, int> ci_map;

#define FOUND(c)	alphabet.find(c) != alphabet.end()

void solve_saving()
{
	int t = GI;
	
	REP(i, t)
	{
		int digits[10] = {0};
		ci_map alphabet;
		
		string s; cin >> s;
		REP(j, s.length())
		{
			int c = 0;
			if (alphabet.find( s[j] ) != alphabet.end())
				c = alphabet[ s[j] ];
			
			alphabet[ s[j] ] = c+1;
		}
		
		_DEBUG(
			ci_map::iterator it;
			ci_map::iterator end = alphabet.end();
			for (it = alphabet.begin(); it != end; it++)
			{
				cout << it->first << " " << it->second << endl;
			}
		);
		
		if (FOUND('Z'))
			digits[0] = alphabet['Z'];
		if (FOUND('W'))
			digits[2] = alphabet['W'];
		if (FOUND('U'))
			digits[4] = alphabet['U'];
		if (FOUND('X'))
			digits[6] = alphabet['X'];
		if (FOUND('G'))
			digits[8] = alphabet['G'];
		
		if (FOUND('H'))
			digits[3] = alphabet['H'] - digits[8];
		if (FOUND('F'))
			digits[5] = alphabet['F'] - digits[4];
		if (FOUND('S'))
			digits[7] = alphabet['S'] - digits[6];

		if (FOUND('I'))
			digits[9] = alphabet['I'] - digits[5] - digits[6] - digits[8];
		
		if (FOUND('N'))
			digits[1] = alphabet['N'] - digits[7] - 2 * digits[9];

		cout << "Case #" << i+1 << ": ";
		REP(j, 10)
			REP(k, digits[j])
				cout << j;
				
		cout << endl;
	}
}

int main()
{
	STARTTIME;
	solve_saving();
	GETTIME;
	return 0;
}
