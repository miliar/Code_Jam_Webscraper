#include <iostream>
#include <cstdio>

double t(double c, double f, double x, int n) {
	double time = 0.0;
	double speed = 2.0;
	while(n > 0) {
		n--;
		time += c / speed;
		speed += f;
	}
	time += x / speed;
	return time;
}

void solve(int test) {
	double c, f, x;
	std::cin >> c >> f >> x;
	double best = t(c, f, x, 0);
	for(int i = 1; i < 10000; ++i) {
		double cost = t(c, f, x, i);
		if(cost < best) {
			best = cost;
		}
		if(cost > best)
			break;
	}
	
	printf("Case #%d: %.7f\n", test, best);
}

int main() {
	int t;
	std::cin >> t;
	std::cout.precision(7);
	for(int i = 1; i <= t; ++i)
		solve(i);
}
