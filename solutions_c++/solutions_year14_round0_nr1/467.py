#include <iostream>
#include <set>

using namespace std;

int main() {
	int Tc;
	int a;
	int p[4][4];
	set<int> ans[2];
	int answer, num_ans;
	cin >> Tc;
	for (int re = 1; re <= Tc; ++re) {
		num_ans = 0;
		ans[0].clear();
		ans[1].clear();
		for (int k = 0; k < 2; ++k) {
			cin >> a;
			for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 4; ++j) {
					cin >> p[i][j];
				}
			}
			for (int j = 0; j < 4; ++j) {
				ans[k].insert(p[a - 1][j]);
			}
		}

		for (auto it = ans[0].begin(); it != ans[0].end(); ++it) {
			if (ans[1].count(*it)) {
				num_ans++;
				answer = *it;
			}
		}

		cout << "Case #" << re << ": ";
		if (num_ans == 1) {
			cout << answer;
		} else if (num_ans == 0) {
			cout << "Volunteer cheated!";
		} else {
			cout << "Bad magician!";
		}
		cout << endl;
	}

	return 0;
}