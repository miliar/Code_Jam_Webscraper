#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>
#include <list>
using namespace std;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testsCnt;
	scanf("%d", &testsCnt);
	for (int testN = 1; testN <= testsCnt; testN++) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double v = 2.0, lastFarmTime = 0.0, res = x / v;
		for (int farms = 0; farms <= 100000; farms++) {
			lastFarmTime += c / v;
			v += f;
			res = min(res, lastFarmTime + x / v);
		}
		printf("Case #%d: %.8lf\n", testN, res);
	}	
}
