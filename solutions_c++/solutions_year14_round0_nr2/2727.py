#include <iostream>
#include <cstdio>
using namespace std;

double c, f, x;

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> c >> f >> x;
		double time = 0.;
		double production = 2.;
		
		// Current time to win > time to add a farm 
		while (x / production > c / production + x / (production + f)) {
			time += (c / production);
			production += f;
		}

		printf("Case #%d: %.8f\n", i, time+x/production);
	}

	return 0;
}

