//prob B cookie_clicker_alpha
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int 	n;
	double	best, solution, production, C, F, X, time, start;
	
	scanf("%d",&n);
	for (int i=1; i<=n; i++) {
		scanf("%lf%lf%lf",&C,&F,&X);
		production = 2;
		start = 0;
		best = (X/production);
		
		bool stop = false;
		while (!stop) {
			time = (C/production) + start;
			production+=F;
			solution = time + (X/production);
			if (solution < best) {
				best = solution;
			}
			else stop = true;
			
			start = time;
		}
		printf("Case #%d: %.6lf\n",i,best);
	}
	return 0;
}
