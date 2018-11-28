#include <iostream>
#include <vector>

using namespace std;

void read(int t[][4]) {
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			cin >> t[i][j];
		}
	}
}
int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("small.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int v1, v2, t1[4][4], t2[4][4];
		cin >> v1;
		read(t1);
		cin >> v2;
		read(t2);
		vector<int> ans;
		for (int i = 1; i <= 16; ++i) {
			int cnt = 0;
			for (int j = 0; j < 4; ++j) {
				if (t1[v1-1][j] == i) ++cnt;
				if (t2[v2-1][j] == i) ++cnt;
			}
			if (cnt == 2) ans.push_back(i);
		}
		cout << "Case #" << t << ": ";
		if (ans.size() > 1) {
			cout << "Bad magician!" << endl;
		} else if (ans.size() == 1) {
			cout << ans[0] << endl;
		} else {
			cout << "Volunteer cheated!" << endl;
		}
	}
}
