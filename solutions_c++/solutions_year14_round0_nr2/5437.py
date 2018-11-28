#include <iostream>
#include <limits>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <vector>
using namespace std;

double c, f, x;

double check(int a) {
	if (a < 0)
		return DBL_MAX;
	double ret = x / (2 + a * f);
	for (int i = 0; i <= a - 1; i++)
		ret += c / (2 + i * f);
	return ret;
}

void work() {
	cin >> c >> f >> x;
	int t = (-2 * c - c * f + f * x) / (c * f);

	double ans = check(0);
	ans = min(ans, check(t));
	ans = min(ans, check(t + 1));
	ans = min(ans, check(t - 1));

	cout << ans << endl;
}

int main() {
	
	//freopen("G:/1.in", "r", stdin);
	//freopen("G:/1.txt", "w", stdout);
	int T;
	cin >> T;
	cout << fixed << setprecision(7);
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		work();
	}
	return 0;
}