#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <deque>

using namespace std;

#define eps 1e-9

int T;

int main () {
	freopen ("input.in", "r", stdin);
	freopen ("output.out", "w", stdout);
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++) {
	    double c, f, x, d = 2.0, res = 0.0;
        scanf ("%lf %lf %lf", &c, &f, &x);
        while (x / d - (c / d + x / (d + f)) > eps) {
            res += c / d;
            d += f;
        }
        res += x / d;
        printf ("Case #%d: %.7lf\n", t, res);
	}
	return 0;
}
