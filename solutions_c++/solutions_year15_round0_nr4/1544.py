/* QC 2015  youri */
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

void solve(int casen)
{
	
	int x, r, c;
	scanf("%d %d %d", &x, &r, &c);
	
	string person[5][5];

	person[1][1]  =  "GRRR";
	person[1][2]  =  "GGRR";
	person[1][3]  =  "GRRR";
	person[1][4]  =  "GGRR";
	
	person[2][2]  =  "GGRR";
	person[2][3]  =  "GGGR";
	person[2][4]  =  "GGRR";
	
	person[3][3]  =  "GRGR";
	person[3][4]  =  "GGGG";
	
	person[4][4]  =  "GGRG";
	
	if(person[MIN(r, c)][MAX(r, c)][x - 1] == 'R')
	{
		printf("Case #%d: RICHARD\n", casen);
	}
	else if(person[MIN(r, c)][MAX(r, c)][x - 1] == 'G')
	{
		printf("Case #%d: GABRIEL\n", casen);
	}
	else
	{
		printf("Case #%d: oupL\n", casen);
	}

			
}

















