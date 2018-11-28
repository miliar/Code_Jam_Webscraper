#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	int t, T;
	scanf("%d", &T);
	for (t = 0; t < T; t ++) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double ret = 0;
		double speed = 2;
		if (x - c < - 0.0000001) {
			printf("Case #%d: %.7lf\n", t + 1, x / speed);
			continue;
		}
		while (true) {
			if (x / speed - (c / speed + x / (speed + f)) > 0.0000001) {
				ret += c / speed;
				speed += f;
			} else {
				ret += x / speed;
				break;
			}
		}
		printf("Case #%d: %.7lf\n", t + 1, ret);
	}
}
