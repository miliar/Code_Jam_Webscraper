#include <iostream>
#include <bitset>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N, M;
		cin >> N;
		M = N;
		bitset<10> seen;
		seen.reset();
		int i = 1;
		for (; i <= 100; ++i) {
			int x = N;
			while (x > 0) {
				seen.set(x % 10);
				x /= 10;
			}
			if (seen.count() == 10) {
				break;
			}
			N += M;
		}
		cout << "Case #" << t << ": ";
		if (seen.count() == 10) {
			cout << N << "\n";
		} else {
			cout << "INSOMNIA\n";
		}
	}
	return 0;
}