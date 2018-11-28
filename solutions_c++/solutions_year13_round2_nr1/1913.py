#include <iostream>
#include <vector>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

int solve(long long curr_mote, vector<int>& motes, int index) {
	if (index >= motes.size()) {
		return 0;
	}

	int mote = motes[index];

	if (curr_mote > mote) {
		return solve(curr_mote + mote, motes, index + 1);
	}

	int method1 = 1 + solve(curr_mote, motes, index + 1);

	if (curr_mote == 1) {
		return method1;
	}

	int move = 0;

	while (curr_mote <= mote) {
		curr_mote += curr_mote - 1;
		move++;
	}

	curr_mote += mote;

	int method2 = move + solve(curr_mote, motes, index + 1);

	if (method1 < method2)
		return method1;

	return method2;
}

int main() {
	int case_cnt;

	cin >> case_cnt;

	for (int i = 1; i <= case_cnt; i++) {
		long long init_mote;
		int mote_cnt;
		vector<int> motes;

		cin >> init_mote >> mote_cnt;

		for (int j = 0; j < mote_cnt; j++) {
			int mote;

			cin >> mote;
			motes.push_back(mote);
		}

		std::sort(motes.begin(), motes.end());
		cout << "Case #" << i << ": " << solve(init_mote, motes, 0) << endl;
	}
}
