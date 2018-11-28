#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
#define FOR(i, a, b) for(int i = a; i <= b; i ++) 

int test;
double c, f, x;

int main() {
	freopen("test.inp", "r", stdin);
	freopen("test.out", "w", stdout);

	cin >> test;
	FOR(t, 1, test) {
		printf("Case #%d: ", t);
		cin >> c >> f >> x;
		double res = 1000000000.0, Rate = 2, Time = 0;
		FOR(i, 1, 200000) {
			res = min(res, Time + x/Rate);
			Time += c / Rate;
			Rate += f;
		}
		printf("%.7lf\n", res);
	}
	return 0;
}