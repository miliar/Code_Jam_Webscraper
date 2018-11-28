#include <list>
#include <map>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int te = 1; te <= tests; te++) {
		double cost, farm, target;
		cin >> cost >> farm >> target;
		int farmCount = target / cost - 2.0 / farm;
		if (target <= cost) {
			// keine farm
			printf("Case #%d: %.7f\n", te, target / 2.0);
		} else {
			if (target / cost - 2.0 / farm < 0) farmCount = 0;		
			double minTime = target / (2.0 + farmCount * farm);
			for (int fa = 1; fa < farmCount + 1; fa++) {
				minTime += cost / (2.0 + (fa - 1) * farm);
			}
			printf("Case #%d: %.7f\n", te, minTime);
		}
	}
}


