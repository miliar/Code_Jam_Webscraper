#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;
int casenum,T;

int main() {
	freopen("gcj14.in","r",stdin);
	freopen("gcj14.out","w",stdout);
	cin >> T;
	for (casenum = 1; casenum <= T; casenum++) {
		cout << "Case #" << casenum << ": ";
		double C, F, X;
		cin >> C >> F >> X;
		double speed = 2;
		double ans = 0;
		while (C < X) {
			double t0 = X / speed;
			double t = C / speed + X / (speed + F);
			if (t0 < t)
				break;
			ans += C / speed;
			speed += F;
		}
		ans += X / speed;
		printf("%.7f", ans);
		cout << endl;
	}
	return 0;
}
