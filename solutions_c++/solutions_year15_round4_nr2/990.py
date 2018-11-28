#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

ifstream inf("B-small-attempt3.in");
ofstream ouf("output.txt");

void solve() {
	int N; double V, X;
	inf >> N >> V >> X;
	if (N == 1) {
		double v, x;
		inf >> v >> x;
		if (x != X) {
			ouf << "IMPOSSIBLE";
		}
		else {
			ouf << V / v;
		}
	}
	else if (N == 2) {
		double v0, x0, v1, x1;
		inf >> v0 >> x0 >> v1 >> x1;
		if (x0 == x1) {
			if (x0 != X) {
				ouf << "IMPOSSIBLE";
			}
			else {
				ouf << V / (v0 + v1);
			}
		}
		else {
			double t1 = (V * (X - x0)) / (v1 * (x1 - x0));
			double t0 = (V - v1 * t1) / v0;
			if (t1 < -(1e-8) || t0 < -(1e-8)) {
				ouf << "IMPOSSIBLE";
			}
			else {
				ouf << max(t0, t1);
			}
		}
	}
}

int main() {
	int T; inf >> T;
	ouf << fixed << setprecision(8);
	for (int t = 1; t <= T; ++t) {
		ouf << "Case #" << t << ": ";
		solve();
		ouf << "\n";
	}
	return 0;
}