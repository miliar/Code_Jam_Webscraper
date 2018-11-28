/* QB 2015  youri */
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
	int res = 1000000;
	int count;

	int pan[1100];
	int max = -1;
	

	scanf("%d", &count);
	//printf("C%d", count);
	REP(i, count)
	{
		int in;
		scanf("%d", &in);
		pan[i] = in;		
		max = MAX(max, in);
	}

	//printf("%d %d\n", *uniqs.rbegin(), freqs[*uniqs.rbegin()]);

	
	FOR(level, 1, max)
	{
		int sum = 0;
		REP(i, count)
		{
			int many = pan[i] / level;
			if(many * level == pan[i])
			{
				many--;
			}

			sum += many;
		}
	//	printf("LEVEL %d, sum %d, level + sum = %d\n", level, sum, level + sum);
		
		res = MIN(res, level + sum);
	}
	

		
	printf("Case #%d: %d\n", c, res);
}

















