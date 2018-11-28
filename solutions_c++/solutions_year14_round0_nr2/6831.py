#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int totalT; 
	cin >> totalT;

	for (int t = 1; t <= totalT; ++ t) {
		double c, f, x; 
		cin >> c >> f >> x;

		double ans = x / 2.0;
		double nowPayment = 2.0, nowSave = 0.0, nowTime = 0.0;

		for (int i = 1; i <= 100000; ++ i) {
			double thisTime = c / nowPayment;
			nowTime += thisTime;
			nowPayment += f; 
			ans = min(ans, nowTime + x / nowPayment); 
		}

		printf("Case #%d: %.7lf\n", t, ans);

	}
}