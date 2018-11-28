#include <iostream>
#include <vector>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b_large.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		double C, F, X;
		cin >> C >> F >> X;
		double tt = 0;
		double st = 2;
		while (true) {
			double t1 = X/st;
			double t2 = C/st + X/(st+F);
			if (t1 <= t2) {
				tt += t1;
				break;
			} else {
				tt += C/st;
				st += F;
			}
		}
		printf("Case #%d: %.7lf\n", t, tt);		
	}
}
