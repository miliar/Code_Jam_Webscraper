// /GCJ-2014/TEST/MAGICTRICK

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <climits>
#include <map>
#include <set>
#include <utility>

using namespace std;

void readnum(vector<int>& choice, int row) {
	int num = 0;
	for (int i = 1; i < row; i++)
		for (int j = 1; j <= 4; j++)
			cin >> num;

	for (int j = 1; j <= 4; j++) {
			cin >> num;
			choice[num] += 1;
	}

	for (int i = row + 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
			cin >> num;
	return;
}

int main() {
	int n_tc = 0;
	cin >> n_tc;

	for (int tc = 1; tc <= n_tc; tc++) {
		vector<int> choice(17, 0);
		for (int i = 0; i < 2; i++) {
			int row = 0;
			cin >> row;
			readnum(choice, row);
		}

		int res = 0, ans = 0;
		for (int num = 1; num <= 16; num++)
			if (choice[num] > 1)
				res += choice[num], ans = num;

		if (res == 2)
			cout << "Case #" << tc << ": " << ans << endl;
		else if (res > 2)
			cout << "Case #" << tc << ": " << "Bad magician!" << endl;
		else
			cout << "Case #" << tc << ": " << "Volunteer cheated!" << endl;
	}
	return 0;
}