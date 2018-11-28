#include <iostream>

using namespace std;

int main() {
	int t; cin >> t;
	for (int tt = 0; tt < t; ++tt) {
		long long x; cin >> x;
		int z = 0;
		long long result = -1;
		for (int i = 1; i < 100000; ++i) {
			long long y = x * i;
			while (y) {
				z |= (1 << (y % 10));
				y /= 10;
			}
			if (z == 1023) {
				result = x * i;
				break;
			}
		}
		if (result == -1) {
			cout << "Case #" << (tt + 1) << ": INSOMNIA" << endl;
		} else {
			cout << "Case #" << (tt + 1) << ": " << result << endl;
		}
	}
	return 0;
}
