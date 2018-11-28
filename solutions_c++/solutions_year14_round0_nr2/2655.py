#include <fstream>
#include <algorithm>
#include <iomanip>
#include <iostream>
using namespace std;

const double eps = 1e-6;

int main() {
	ifstream inf("B-large.in");
	ofstream outf("output.txt");

	int T; inf >> T;
	for (int tc = 1; tc <= T; tc++) {
		outf << "Case #" << tc << ": ";
		double C, F, X;
		inf >> C >> F >> X;
		double time = 0;
		double speed = 2.0;
		double ans = X / 2.0;
		while (true) {
			double prev_ans = ans;
			//ans = min(ans, time + X / speed);
			double tmp = time + X / speed;
			if (tmp < ans) {
				double prev_ans = ans;
				ans = tmp;
				//if (prev_ans - ans < eps) break;
			}
			time += C / speed;
			if (time > ans) break;
			speed += F;
		}
		outf << fixed << setprecision(7) << ans << '\n';
	}
}