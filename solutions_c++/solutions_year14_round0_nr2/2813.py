#include <fstream>
//#include <iostream>
#include <map>

using namespace std;

ifstream cin("B-large.in");
ofstream cout("output.txt");


void solve(int t) {
	double c, f, x;
	cin >> c >> f >> x;
	int k = ((f * x) / c - 2.) / f + 1.;
	k--;
	if (k < 0) {
		k = 0;
	}
	double ans = x / (2. + k * f);
	for (int i = k - 1; i >= 0; --i) {
		ans += c / (2. + i * f);
	}
	cout.precision(20);
	cout << "Case #" << t << ": " << ans << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		solve(i+1);
	}
	return 0;
}