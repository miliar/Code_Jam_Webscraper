#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		printf("Case #%d: ", nc);
		int r1;
		cin >> r1, --r1;
		vector<int> a, b;
		for (int r = 0; r < 4; ++r) {
			for (int c = 0; c < 4; ++c) {
				int x;
				cin >> x;
				if (r == r1)
					a.push_back(x);
			}
		}
		cin >> r1, --r1;
		for (int r = 0; r < 4; ++r) {
			for (int c = 0; c < 4; ++c) {
				int x;
				cin >> x;
				if (r == r1)
					b.push_back(x);
			}
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int c[4], cnt;
		cnt = set_intersection(a.begin(), a.end(), b.begin(), b.end(), c) - c;
		if (cnt == 1) {
			cout << c[0] << endl;
		} else if (cnt == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
}
