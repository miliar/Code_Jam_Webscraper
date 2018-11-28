#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define forl(i,a,b) for(int i = a; i < b; ++i)

int main()
{
	int numcases = 0;
	double cps, fcc, fcps, xcg, time;
	cin >> numcases;
	forl(casei, 0, numcases) {
		cin >> fcc >> fcps >> xcg;
		if (fcc >= xcg) {
			time = xcg/2.0;
		} else {
			time = 0.0;
			cps = 2.0;
			while ((xcg-fcc)/cps > xcg/(cps+fcps)) {
				time += fcc/cps;
				cps += fcps;
			}
			time += xcg/cps;
		}
		printf("Case #%d: %.7f\n", casei+1, time);
	}
	return 0;
}
