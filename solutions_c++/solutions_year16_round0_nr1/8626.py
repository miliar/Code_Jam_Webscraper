#include <iostream>
#include <vector>
#define LL long long

using namespace std;

int main() {
	std::iostream::sync_with_stdio(false);
	LL t; cin >> t;
	for (LL k = 1; k <= t; ++k) {
		vector<bool> seen(10, false);
		cout << "Case #" << k << ": ";
		LL n; cin >> n;
		if (n == 0) {cout << "INSOMNIA" << endl; continue;}

		LL found = 0, clone;
		LL i = 0;
		while (found != 10) {			
			++i;
			clone = n*i;
			while (clone > 0) {
				if (!seen[clone % 10]) {
					seen[clone % 10] = true;
					found++;
				}
				clone /= 10;
			}
		}
		cout << n*i << endl;
	}
}