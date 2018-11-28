#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <cmath>

using namespace std;

bool ok(int len, int x, int y, bool print)
{
	if (!len) return (x == 0) && (y == 0);
	if (abs(x) > abs(y))
		if (x < 0) {
			bool res = ok(len-1, x+len, y, print);
			if (print) printf("W");
			return res;
		}
		else {
			bool res = ok(len-1, x-len, y, print);
			if (print) printf("E");
			return res;
		}
	else {
		if (y < 0) {
			bool res = ok(len-1, x, y+len, print);
			if (print) printf("S");
			return res;
		}
		else {
			bool res = ok(len-1, x, y-len, print);
			if (print) printf("N");
			return res;
		}
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int ntest; 
	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++) {
		int x, y; 
		scanf("%d%d", &x, &y);
		printf("Case #%d: ", test);
		for(int len = 1; len <= 1000000; len++)
			if (ok(len, x, y, false)) {
				ok(len, x, y, true);
				break;
			}
		printf("\n");
	}
	return 0;
}
