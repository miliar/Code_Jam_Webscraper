#include <stdio.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <sstream>
using namespace std;

double solve(double c, double f, double x) {
	double time = 0, rate = 2;
	if (x <= c)
		return x / rate;
	vector<double> times;
	while (true) {
		double time1 = x / rate;
		double time2 = c / rate + x / (rate+f);
		if (time1 < time2) {
			times.push_back(time1);
			break;
			//return time + time1;
		}
		else {
			times.push_back(c / rate);
			rate += f;
		}
	}
	sort(times.begin(), times.end());
	double sum = 0;
	for (int i = 0; i < times.size(); ++i)
		sum += times[i];
	return sum;
}

int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		double c, f, x; scanf("%lf %lf %lf", &c, &f, &x);
		printf("Case #%d: %0.7lf\n", t, solve(c, f, x));
	}
	return 0;
}