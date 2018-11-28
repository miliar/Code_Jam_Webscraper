#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 16

#define max(a,b) ((a) >= (b) ? (a) : (b))
#define min(a,b) ((a) <= (b) ? (a) : (b))

using namespace std;

int v[N+1];

int main () {

	int t, tst, y, z, i, j, p, m, n=4, r, r2;
	double tm, c, x, f, fmin, ks=2;
	
	
	scanf("%d", &tst);

	for (t = 0; t < tst; t++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		
		fmin = f*(x-c)/c;
		ks = 2;
		tm = 0;
		
		while (ks < fmin) {
			tm += c / ks;
			ks += f;
		}
		
		tm += x / ks;
		
		printf("Case #%d: %.7lf\n",t+1, tm);
		
	}
	
	return 0;

}
		

