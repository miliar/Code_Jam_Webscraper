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
	char inp[200];
	scanf("%s", inp);
	
	int sol = 0;
	int i = 0;
	char ch;
	char prev = inp[0];
	
	while (ch = inp[i])
	{
		if(ch != prev)
		{
			sol++;
		}
		
		prev = ch;
		i++;
		//printf ("%c,", ch);
	}
	//printf ("%c,", inp[i-1]);
	if(inp[i-1] == '-')
	{
		sol++;
	}
	
	printf("Case #%d: %d\n", c, sol);

}
