#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

#define INFL "in"
#define OUTFL "out"

using namespace std;

void read() {
}

#define eps 1e-7

int tests;
double C, F, X;

void solve() {
	cin >> tests;
	for(int t=1; t<=tests; ++t) {
		cin >> C >> F >> X;

		double pre = X / 2.0;
		double acc = 0.0, total;
		int cookies = 0;

		while(true) {
			++cookies;

			acc += C / (2.0 + (cookies - 1)*1.0*F);

			total = acc + X / (2 + cookies*1.0*F);

			if(total - pre > eps && fabs(total - pre) > eps) break;
			pre = total;
		}

		printf("Case #%d: %.7lf\n", t, pre);
	}
}

int main() {
//#define ONLINE_JUDGE 1
#ifndef ONLINE_JUDGE
	freopen(INFL, "r", stdin);
	freopen(OUTFL, "w", stdout);
#endif

	read();
	solve();
	
	return 0;
}