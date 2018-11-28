//Karol Kaszuba
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef double D;
typedef long double LD;
typedef vector<PII> VII;

#define FOR(i,x,y) for(int i=(x);i<=(y);++i)
#define REP(i,x) FOR(i,0,(x)-1)
#define FORD(i,x,y) for(int i=(x);i>=(y);--i)
#define VAR(i,c) __typeof(c) i=(c)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)

#define SIZE(c) (int)((c).size())
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define IN insert
#define ER erase
#define MP make_pair
#define ST first
#define ND second
#define IOSYNC ios_base::sync_with_stdio(0)

LD jebaj()
{
	LD c,f,x, cookies_per_second = 2.0, 
		my_cookies = 0.0, time_spent_on_buildings = 0.0;
	scanf("%Lf %Lf %Lf", &c, &f, &x);
	
	LD best_time = x/cookies_per_second;
	
	FOR(i, 1, x + 10)
	{
		time_spent_on_buildings += (c / cookies_per_second);
		cookies_per_second += f;
		best_time = min(best_time, time_spent_on_buildings + (x / cookies_per_second));
	}
	return best_time;
	
	// c/cps + c/(cps + f) + (c/(cps + 2f)
	
}

int main()
{
	int t;
	scanf("%d", &t);
	REP(i, t) printf("Case #%d: %.8Lf\n", i + 1, jebaj());
}
