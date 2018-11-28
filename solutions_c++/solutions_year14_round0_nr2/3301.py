#include <cstdio>
#include <iostream>

typedef unsigned int uint;

using namespace std;

long double solve(long double c, long double f, long double x) {
	long double rate = 2, t = 0;

	if(c >= x)
		return x/rate;

	while(true) {
		long double not_buy = (x-c)/rate;
		long double buy = x/(rate + f);

		if(not_buy <= buy) {
			t += (c/rate) + not_buy;

			break;
		}

		t += c/rate;
		rate += f;
	}

	return t;
}

int main() {
	int cases;
	long double c, f, x;

	cin >> cases;

	for(int i = 0; i < cases; ++i) {
		cout << "Case #" << i+1 << ": ";

		cin >> c >> f >> x;

		printf("%.7Lf\n", solve(c, f, x));
	}

	return 0;
}