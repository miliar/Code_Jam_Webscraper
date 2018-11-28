#include <cstdio>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;
double c, f, x;

void init() {
	scanf("%lf%lf%lf", &c, &f, &x);
	return;
}

double calc() {
	double currate = 2.0;
	double ans = x / currate;
	double curtime = 0;
	while (true) {
		curtime += (c / currate);
		currate += f;
		if (ans < (curtime + (x / currate))) {
			return ans;
		} else {
			ans  = curtime + (x / currate);
		}
	}
}

int main(){
	int tcase;
	scanf("%d", &tcase);
	for (int i = 1; i <= tcase; i++) {
		init();
		printf("Case #%d: %.7lf\n", i, calc());
	}
	return 0;
}
