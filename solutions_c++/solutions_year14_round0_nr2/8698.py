#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

#define MAX_N 100000

int tests;
double cost, boost, goal;

double go(double cost, double boost, double goal) {
		if (goal <= cost ) return goal / 2.0;
		
		double currentSpeed = 2.0;
		double timeSpent = cost / currentSpeed;
		double newTime = goal / (currentSpeed + boost);
		double timeLeft = (goal - cost) / currentSpeed;
		
		while(timeLeft >= newTime) {
			currentSpeed += boost;
			timeSpent += cost / currentSpeed;
			newTime = goal / (currentSpeed + boost);
			timeLeft = (goal - cost) / currentSpeed;
		}
		
		return timeSpent + timeLeft;
}

int main() {
	scanf("%d",&tests);
	for (int test = 1; test <= tests; test++) {
		scanf("%lf %lf %lf", &cost, &boost, &goal);		
		printf("Case #%d: %.7lf\n", test, go(cost, boost, goal));	
	}
	return 0;
}