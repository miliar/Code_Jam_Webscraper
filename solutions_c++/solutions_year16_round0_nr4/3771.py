#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

vector<int> tilesToCheck(int k, int c, int s) {
	vector<int> tiles;
	if (k == s) {
		// easy case for small dataset, start sequence will also be the same
		for (int i = 1; i <= k; i++) {
			tiles.push_back(i);
		}
	} else {

	}
	return tiles;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int k, c, s;
		cin >> k >> c >> s;
		auto tiles = tilesToCheck(k, c, s);
		printf("Case #%d:", t);
		if (tiles.empty()) {
			cout << " IMPOSSIBLE";
		} else {
			for (auto& x : tiles) {
				cout << " " << x;
			}
		}
		cout << endl;
	}
}
