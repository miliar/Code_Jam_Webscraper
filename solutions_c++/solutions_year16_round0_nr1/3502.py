#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;

typedef long long ll;

int main() {
#ifdef _DEBUG
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		ll a;
		cin >> a;
		if (a == 0) {
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		}
		else {
			ll r = 0;
			bool d[10];
			memset(d, 0, 10 * sizeof(bool));
			int dd = 0;

			int k = 0;
			bool found = false;

			while (k < 1000000 && !found) {
				k++;
				r += a;
				ll rr = r;
				while (rr > 0) {
					int c = rr % 10;
					rr /= 10;
					if (!d[c]) {
						d[c] = true;
						dd++;
					}
				}

				found = (dd == 10);
			}

			if (found) {
				cout << "Case #" << t << ": " << r << endl;
			}
			else {
				cout << "Case #" << t << ": " << "INSOMNIA" << endl;
			}
			
		}
	}
	return 0;
}