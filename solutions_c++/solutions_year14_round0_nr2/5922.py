#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

int main() {
	freopen("in2.in", "r", stdin);
	freopen("ou2", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++) {
		double c, f, x, best, v = 2.0, time = 0.0;
		scanf("%lf %lf %lf", &c, &f, &x);
		best = x/2;
		int a = 0;
		while(true) {
			a++;
			if(a == 100000) break;
			best = min(best, time + x/v);
			time += c/v;
			v += f;
			//printf("%lf\n", time);
		}
		printf("Case #%d: %.7lf\n", test, best);
	}
	return 0;
}
		
