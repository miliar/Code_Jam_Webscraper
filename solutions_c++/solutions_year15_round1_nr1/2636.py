#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
	int t = 0;
	cin >> t;
	cerr << "Tests=" << t << endl;
	for (int tt = 0 ; tt < t ; ++tt) {
		int n = 0;
		cin >> n;
		cerr << "n=" << n << endl;
		vector<int> m(n, 0);
		int maxdiff = -1;
		int sum = 0;
		for (int i = 0 ; i < n ; ++i) {
			int mi = 0;
			cin >> mi;
			m[i] = mi;
			cerr << "mi=" << mi << endl;
			if (i > 0 && m[i - 1] - mi > maxdiff) {
				maxdiff = m[i - 1] - mi;
			}
			sum += mi;
		}
		int z = 0;
		int y = 0;
		for (int i = 0 ; i < n - 1 ; ++i) {
			int ya = m[i] - m[i + 1];
			if (ya > 0) y += min(ya, maxdiff);
			z += min(maxdiff, m[i]);
		}
		cout << "Case #" << (tt + 1) << ": " << y << " " << z << endl;
	}
}
