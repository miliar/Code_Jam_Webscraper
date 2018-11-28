#include <cstdio>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

#define MINX(a, b) ((a) < (b) ? (a) : (b));
#define MAX(a, b) ((a) > (b) ? (a) : (b));

typedef unsigned long long ulng;
typedef signed long long slng;
typedef unsigned int uint;
typedef signed int sint;

void solve()
{
	double c, f, x, n;
	double farm, wait, rate, sum;
	cin >> c >> f >> x;

	sum = 0;
	n = 0.0;
	rate = 2.0;
	wait = x / rate;
	while (1) {
		wait = (x - n) / rate;
		farm = c / rate;
		if (farm + (x / (rate + f)) < wait) {
			sum += farm;
			rate += f;
			n = 0.0;
		} else {
			sum += wait;
			break;
		}
	}
	cout << fixed << setprecision(7) << sum;
}

int main()
{
	int c;
	cin >> c;
	for (int i = 1; i <= c; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << "\n";
	}
}
