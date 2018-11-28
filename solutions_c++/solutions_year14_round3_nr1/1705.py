#include <iostream>

using namespace std;

const double eps = 1e-9;

int main() {
	int N;
	cin >> N;
	for (int n = 1; n <= N; n++) {
		long long P, Q;
		char crap;
		cin >> P >> crap >> Q;
		if ((P * (1LL<<40)) % Q == 0) {
			for (int i = 0; i <= 40; ++i) {
				//cerr << i << ": " << (1.0l / (1<<i)) << " <= " << (double(P)/double(Q) - eps) << endl;
				if ((1.0l / (1<<i)) <= double(P)/double(Q) + eps) {
					cout << "Case #" << n << ": " << i << endl;
					break;
				}
			}
		} else {
			cout << "Case #" << n << ": impossible" << endl;
		}
	}
}
