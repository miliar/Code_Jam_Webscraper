//venk13
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <cassert>

using namespace std;

#define sz(a) (int)(a.size())
#define len(a) (int)(a.length())
#define pb push_back
#define mp make_pair

double cum[111111];

void pre(double c, double f) {
	double incr = f; cum[0] = c / 2;
	for(int i = 1; i < 111111; i++) {
		cum[i] = cum[i - 1] + c / (2 + incr);
		incr = incr + f;
	}
}

double wait(double x, double f, int y) {
	return (y > 0 ? cum[y - 1] : 0) + x / (2 + y * f);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output1.txt", "w", stdout);
	int t, cas = 1; scanf("%d", &t);
	while(t--) {
		printf("Case #%d: ", cas++);
		double c, f, x; scanf("%lf%lf%lf", &c, &f, &x);
		if(x <= c) {
			printf("%.7f\n", x / 2);
			continue;
		}
		pre(c, f);
		int lo = 0, hi = 111110, ret = -1;
		while(lo <= hi) {
			int mid = (lo + hi) >> 1;
			if(wait(x, f, mid) <= wait(x, f, mid + 1))
				ret = mid, hi = mid - 1;
			else
				lo = mid + 1;
		}
		assert(ret != -1);
		printf("%.7f\n", wait(x, f, ret));
	}
	return 0;
}