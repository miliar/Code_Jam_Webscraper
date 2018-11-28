#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <iostream>

#define ll long long

using namespace std;

int zt;

int main() {
    scanf("%d", &zt);
    
    for (int kt=0; kt<zt; ++kt) {
	double c, f, x, rate = 2.;
	double res;
	scanf("%lf%lf%lf", &c, &f, &x);
	
	double time = 0;
	
	while (x/rate > c/rate + x/(rate+f)) {
	    time += c/rate;
	    rate += f;
	}
	time += x/rate;
	
	printf("Case #%d: %lf\n", kt+1, time);
    }
}