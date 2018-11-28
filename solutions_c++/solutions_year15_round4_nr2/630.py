#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int n;
double v, x;

struct node {
	double delta, rate;
	bool operator < (const node &p) const {
		return delta < p.delta;
	}
};

node positive[10000], negative[10000];
int pc = 0, nc = 0;
double rspd = 0;

double solve() {
	cin >> n >> v >> x;
	pc = nc = 0;
	rspd = 0;
	
	for (int i = 0; i < n; i++) {
		double r, c;
		cin >> r >> c;
		if (fabs(c - x) < 1e-6) rspd += r;
		else if (c - x > 1e-6) {
			positive[pc].delta = c - x;
			positive[pc].rate = r;
			pc++;
		} else {
			negative[nc].delta = x - c;
			negative[nc].rate = r;
			nc++;
		}
	}
	
	sort (positive, positive + pc);
	sort (negative, negative + nc);
	
	// printf("pc = %d, nc = %d.\n", pc, nc);
	
	double spd = 0;
	if (pc > 0 && nc > 0) {
		for (int i = 1; i <= pc; i++) {
			for (int j = 1; j <= nc; j++) {

				double pd = 0, pr = 0;
				double nd = 0, nr = 0;
		
				for (int ii = 0; ii < i; ii++) {
					pd += positive[ii].delta * positive[ii].rate;
					pr += positive[ii].rate;
				}
				for (int jj = 0; jj < j; jj++) {
					nd += negative[jj].delta * negative[jj].rate;
					nr += negative[jj].rate;
				}
				
				// printf("i = %d, pd = %f, pr = %f\n", i, pd, pr);
				// printf("j = %d, nd = %f, nr = %f\n", j, nd, nr);
				
				double tmp = 0;
				if (pd > nd)	tmp = nr + pr * (nd / pd);
				else 			tmp = pr + nr * (pd / nd);
				
				spd = max(spd, tmp);
			}
		}
	}
	double tspd = spd + rspd;
	if (tspd < 1e-6) return -1;
	return v / tspd;
}

int main() {
	int t;
	cin >> t;
	for (int cas = 1; cas <= t; cas++) {
		double ret = solve();
		printf("Case #%d: ", cas);
		if (ret > 1e-6)
			printf("%f\n", ret);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}