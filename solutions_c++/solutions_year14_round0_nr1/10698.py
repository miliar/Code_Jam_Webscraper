#include <iostream>
#include <vector>

using namespace std;

void solve() {
	int ans1; cin >> ans1;
	ans1--;
	vector<int> vi;
	int t;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> t;
			if (i == ans1) vi.push_back(t);
		}
	}
	int ans2; cin >> ans2;
	ans2--;
	vector<int> vi2;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> t;
			if (i == ans2) vi2.push_back(t);
		}
	}

	int res = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (vi[i] == vi2[j]) {
				if (res) {
					cout << " Bad magician!" << endl;
					return;
				} else {
					res = vi[i];
				}
			}
		}
	}
	if (res) cout << " " << res << endl;
	else cout << " Volunteer Cheated!" << endl;
}

int main() {
	int T; cin >> T;

	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ":";
		solve();
	}
	return 0;
}