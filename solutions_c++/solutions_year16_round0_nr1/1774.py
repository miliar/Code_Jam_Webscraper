#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);

	int T; cin >> T;
	for (int t = 1; t <= T; ++t) {
		long long n; cin >> n;

		cout << "Case #" << t << ": ";
		
		if (n == 0) {
			cout << "INSOMNIA" << endl;
		}
		else {
			bool digs[10] = { };
			int c = 0;

			for (auto a = n;; a += n) {
				auto x = a; 

				while (x) {
					if (!digs[x % 10]) {
						digs[x % 10] = 1, ++c;
					}

					x /= 10;
				}

				if (c == 10) {
					cout << a << endl;
					break;
				}
			}
		}
	}
}