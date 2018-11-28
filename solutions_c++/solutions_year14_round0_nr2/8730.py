#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
	int T, num;
	double cost, f, x;
	double time, res;
	double rate;
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> cost >> f >> x;
		rate = 2;
		time = 0;
		res = x/rate;
		num = 1;
		while (true) {
			time += cost/rate;
		//	printf("time: %.8f\n", time);
			rate += f;
		//	printf("rate: %.8f\n", rate);
			if (res > time + x/rate) {
				res = time + x/rate;
			}
			else {
				break;
			}
			++num;
		}
		printf("Case #%d: %.8f\n", t, res);
	}
}

