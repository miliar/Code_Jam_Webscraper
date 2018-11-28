#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <limits>
#include <set>
#include <algorithm>
#include <iterator> 

using namespace std;

int t;
double farmPrice, farmProfit, goal;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;

	for (int test = 1; test <= t; test++) {
		cin >> farmPrice >> farmProfit >> goal;
		 
		double currentSpeed = 2.0;
		double currentTime = 0.0;

		while (true) {
			double withoutFarm = goal / currentSpeed;
			double withFarm = (farmPrice / currentSpeed) + goal / (currentSpeed + farmProfit);

			if (withoutFarm <= withFarm) {
				currentTime += goal / currentSpeed;
				break;
			} else {
				currentTime += farmPrice / currentSpeed;
				currentSpeed += farmProfit;
			}
		}

		printf("Case #%d: %0.7lf\n", test, currentTime);
	}

	return 0;
}