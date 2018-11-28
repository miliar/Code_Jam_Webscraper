/* QA 2015  youri */
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

typedef long long LL;

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(val) ((val) < 0 ? -(val) : (val))

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

void solve(int c);
int main() {

	int cases;
	scanf("%d", &cases);
	REP(i, cases)
	{
		solve(i + 1);
	}

	return 0;
}

void solve(int c)
{
	char ar[2000];
	int nm;
	scanf("%d %s", &nm, ar);

	int stood = 0;
	int friends = 0;
		
	FOR(i, 0, nm)
	{
		int elem = ar[i] - '0';

//		printf("%d", elem);
		if(elem != 0)
		{
			int new_friends = 0;
			if(i > stood)
			{
				new_friends = (i - stood);
			}
			
			stood += elem + new_friends;
			friends += new_friends;

		}
	}
	
	
	printf("Case #%d: %d\n", c, friends);
}

