#include <stdio.h>
#include <math.h>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int a[20] = {0};

int main() {
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	int x, y, z, t;
	double j, k, fl, i, n, p, r, q, l, kol, flag, m;
	scanf("%i", &z);
	for(t = 1; t <= z; t++) {
		scanf("%lf%lf%lf", &n, &m, &l);
		kol = 1000000000.0;
		r = 0;
		p = 2.0;
		for(i = 0; p <= max(l, 110000.0); i++) {
			kol = min(kol, r + l / p);
			r += n / p;
			p += m;
		}
		printf("Case #%i: %.7lf\n", t, kol);
	}
	return 0;
}