#include <iostream>
#include <vector>
using namespace std;

int main () {

	int T, t = 1;
	cin >> T;

	while (t <= T) {

		vector<int> nums (17);
		int pill, c_pill, num;
		cin >> pill;

		for (int i = 0; i < 16; ++i) {
			c_pill = i/4 + 1;
			cin >> num;
			if (pill == c_pill) nums[num]++;
		}

		cin >> pill;

		int solutions = 0, solution = 0;

		for (int i = 0; i < 16; ++i) {
			c_pill = i/4 + 1;
			cin >> num;
			if (pill == c_pill && nums[num] == 1) {
				++solutions;
				solution = num;
			}
		}

		cout << "Case #" << t << ": ";

		switch (solutions) {
			case 0:
				cout << "Volunteer cheated!" << endl;
				break;
			case 1:
				cout << solution << endl;
				break;
			default:
				cout << "Bad magician!" << endl;
				break;
		}

		++t;

	}

}