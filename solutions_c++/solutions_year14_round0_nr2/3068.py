#include <iostream>
#include <iomanip>
#define EPS 1e-9
using namespace std;

int T;
double C, F, X;

bool can(double t) {
	double ratio = 2.0;

	do {
		if ( ((ratio*t)-X) > EPS)
			return true;

		t -= C/ratio;
		ratio += F;
	} while (t > EPS);
	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	cout << setprecision(7) << fixed;
	for (int caso=1; caso<=T; caso++) {
		cin >> C >> F >> X;

		double lo = 0.0, mid, hi = 500000.0;
		while(hi - lo > EPS) {
            mid = (lo+hi)/2.0;
            if (can(mid))
            	hi = mid;
            else
            	lo = mid;
        }

        cout << "Case #" << caso << ": " << lo << "\n";
	}
}