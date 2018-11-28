#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <cassert>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)

int t;
double c, f, x;

int main() {
	cin >> t;
	REP(qqq,t) {
		cin >> c >> f >> x;
		pair<double,int> best = make_pair(x/2, 0);
		double running = 0;
		REP(i,500005) {
			//we buy this number of farms
			double time = running + x/(2 + i*f);
			best = min(best, make_pair(time, i));

			running += c/(2 + i*f);
		}
		printf("Case #%d: %0.9lf\n", qqq+1, best.first, best.second);
		assert(running > best.first);
//		cout << running << endl;
	}
}
