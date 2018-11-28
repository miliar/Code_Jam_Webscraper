#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		int K, C, S; cin >> K >> C >> S;

		cout << "Case #" << tc << ": ";
		if (K - C + 1 > S) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		int c = min({ K, C, S });
		ll k = K, j = 1;

		for (int i = 2; i <= c; ++i) {
			--k;
			j = (j - 1) * K + i;
		}
		for (int i = 0; i < k; ++i)  {
			cout << j++ << ' ';
		}
		cout << endl;
	}
}
