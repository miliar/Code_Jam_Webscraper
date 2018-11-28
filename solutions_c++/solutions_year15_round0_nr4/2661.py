#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	freopen("input2.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	int iii, jjj, n, t, p, x, r, c;
	scanf("%d", &t);
	for (p = 1; p <= t; p++) {
		scanf("%d %d %d", &x, &r, &c);
		if (r > c)
			swap(r, c);
		if (((r*c) % x) != 0) {
			printf("Case #%d: RICHARD\n", p);
			continue;
		}
		if ((x == 3 && r == 1 && c == 3) || (x == 4 && r == 1 && c == 4) || (x == 4 && r == 2 && c == 4) || (x == 4 && r == 2 && c == 2)) {
			printf("Case #%d: RICHARD\n", p);
			continue;
		}
		printf("Case #%d: GABRIEL\n", p);
	}
	return 0;
}