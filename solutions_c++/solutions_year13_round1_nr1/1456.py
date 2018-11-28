#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

#define sqr(x) ((x) * (x))

int main() {
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		int r, ti, ans = 0, x = 1, y = 0;
		scanf("%d%d", &r, &ti);
		while (ti - (2 * r * (x - y) + sqr(x) - sqr(y) ) >= 0) {
			ti -= (2 * r * (x - y) + sqr(x) - sqr(y) );
			ans++;
			x += 2;
			y += 2;
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
