#include <algorithm>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;


#define FOR(i, n) for(int i = 0; i < n; ++i)


void solve(int t, double &cost, double &relax, double &aim) {
	double rate = 2.0, ts, tc, ta = 0.0;
	cout << "CASE #" << t << ": ";
	while (1) {
		ts = aim / rate;  // w/o farms
		tc = cost / rate + aim / (rate + relax);  // w farms
		if (ts <= tc) {
			ta += ts;
			break;
		}
		else {
			ta += cost / rate;
			rate += relax;
		}
	}
	cout << fixed << setprecision(7) << ta << endl;
}


int main() {
	freopen("other/input.txt", "r", stdin);
	freopen("other/output.txt", "w", stdout);
	int t = 1, tn;
	cin >> tn;

	double cost, relax, aim;
	while (t <= tn) {
		cin >> cost >> relax >> aim;
		solve(t++, cost, relax, aim);
	}
	return 0;
}
