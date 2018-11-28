#include <iostream>

using namespace std;

int main() {
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);

	int T, it = 0;
	cin >> T;
	while (T--) {
		int p1, p2;
		int good[17];

		memset(good, 0, sizeof(good));

		cin >> p1;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)  {
				int x;
				cin >> x;
				if (p1 == i + 1) good[x] = 1;
			}

		cin >> p2;
		for (int i = 0; i < 4; ++i)
			for (int j =0; j < 4; ++j) {
				int x;
				cin >> x;
				if (p2 != i + 1) good[x] = 0;
			}

		int cnt = 0, ans = 0;
		for (int i = 1; i<= 16; ++i) if (good[i]) {
			ans = i;
			cnt++;
		}

		++it;
		cout << "Case #" << it << ": ";
		if (cnt == 1) {
			cout << ans << endl;
		} else
		if (cnt == 0) {
			cout << "Volunteer cheated!" << endl;
		} else 
		if (cnt > 1) {
			cout << "Bad magician!" << endl;
		}
	}

	return 0;
}
