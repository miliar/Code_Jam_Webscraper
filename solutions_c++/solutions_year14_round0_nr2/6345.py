#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
	double C, F, X;
	cin >> C >> F >> X;

	double v = 2;
	double ans = X / v;

	double t = C / v;
	v += F;
	for (;;) {
	    double ans2 = t + X / v;
	    if (ans > ans2) {
		ans = ans2;
		t += C / v;
		v += F;
	    }
	    else {
		break;
	    }
	}

	cout << "Case #" << i << ": " << fixed << setprecision(7) << ans << endl;
    }
}
