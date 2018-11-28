#include <iostream>
#include <algorithm>
using namespace std;
const char* INSOMNIA = "INSOMNIA";
int main() {
	int T; cin >> T;
	for (int i = 0; i < T; i++) {
		int BITS = 0;
		long long N; cin >> N;
		if (N > 0) {
			for (int j = 1;; j++) {
				if (BITS == 1023) {
					cout << "Case #" << i + 1 << ": " << N * (j - 1) << "\n";
					break;
				}
				long long S = N * j;
				while (S > 0) {
					BITS = BITS | (1 << (S % 10));
					S = S / 10;
				}
			}
		}
		if (BITS != 1023) {
			cout << "Case #" << i + 1 << ": " << INSOMNIA << "\n";
		}
	}
	return 0;
}
