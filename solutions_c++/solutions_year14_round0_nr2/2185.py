#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>


using namespace std;


void solve() {
	double C,F,X;
	scanf("%lf %lf %lf", &C, &F, &X);
	
	double A = 2.0/F;
	double B = X/C;
	double D = C/F;
	
	int n = 0;
	double time = 0.0;
	for (n=0; n < B-A-1; n++) {
	    // Build a farm
	    time += 1/(n+A);
	}
	// Win
	time += B/(n+A);
	time *= D;
	
	printf("%.7lf\n", time);
}

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=0; i<t; ++i) {
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
