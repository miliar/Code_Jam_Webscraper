#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		double cost, boost, goal;
		cin >> cost >> boost >> goal;
		double rate = 2;
		double ans = 0;
		while (1) {
			double wait = goal / rate;
			double build = cost / rate + goal / (rate + boost);
			if (build < wait) {
				ans += cost / rate;
				rate += boost;
			} else {
				ans += wait;
				break;
			}
		}
		printf("Case #%d: %.7lf\n", cN, ans);
	}
}
