#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <math.h>
#include <cstdio>
using namespace std;

int main() {
	int T = -1;
	scanf("%d", &T);
	int k = 1;
	while (k <= T) {
		double C = 0, F = 0, X = 0;
		scanf("%lf %lf %lf", &C, &F, &X);
		double total = 0;
		double ret = 0;
		if (X < C || fabs(X-C) < 1e-6) {
			ret = X/2.0;
		}
		else {
			double a[2];
			double b[2];
			int base = 0;
			a[0] = 2.0;
			b[0] = 0;
			while(true) {
				ret += C/a[base];
				int next = (base+1)%2;
				double ta = a[base] + F;
				double tb = -1 * ta * ret;
				double tt = (b[base]-tb)/(ta-a[base]);
				double y = ta*tt + tb;
				if( y < X ) {
					a[next] = ta;
					b[next] = tb;
					base = next;
				}
				else {
					ret = (X-b[base])/a[base];
					break;
				}
			}
		}
		printf("Case #%d: %.7lf\n", k, ret);
		k++;
	}
	return 0;
}