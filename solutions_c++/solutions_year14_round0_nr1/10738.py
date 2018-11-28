/* QA 2014  youri */
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
	int discard [4];
	int ans1 [4];
	int ans2 [4];
	int row;
		
	scanf("%d", &row);
	REP(i, 4)
	{
		int * c[4];
		if(i + 1 == row)
			scanf("%d %d %d %d\n", ans1, ans1 + 1, ans1 + 2, ans1 + 3);
		else
			scanf("%d %d %d %d\n", discard, discard + 1, discard + 2, discard + 3);
	}
		
	scanf("%d", &row);
	REP(i, 4)
	{
		int * c[4];
		if(i + 1 == row)
			scanf("%d %d %d %d\n", ans2, ans2 + 1, ans2 + 2, ans2 + 3);
		else
			scanf("%d %d %d %d\n", discard, discard + 1, discard + 2, discard + 3);
	}

	std::vector<int> v(8);
	std::vector<int>::iterator it;
	sort(ans1, ans1 + 4);
	sort(ans2, ans2 + 4);

	it = set_intersection(ans1, ans1 + 4, ans2, ans2 + 4, v.begin());
	v.resize(it - v.begin());

	if(v.size() == 0)
	{
		printf("Case #%d: %s\n", c, "Volunteer cheated!");

	}
	else if (v.size () == 1)
	{
		printf("Case #%d: %d\n", c, v[0]);
	}
	else
	{
		printf("Case #%d: %s\n", c, "Bad magician!");
	}

}

