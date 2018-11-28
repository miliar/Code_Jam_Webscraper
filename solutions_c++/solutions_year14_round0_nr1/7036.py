#include <iostream>
using namespace std;

int main(void) {
	int test_count;
	cin >> test_count;
	for (int test = 1; test <= test_count; ++ test) {
		int row, square[4][4], count[17] = {0};
		for (int t = 0; t < 2; ++ t) {
			cin >> row;
			for (int i = 0; i < 4; ++ i) {
				for (int j = 0; j < 4; ++ j)
					cin >> square[i][j];
			}
			row --;
			for (int i = 0; i < 4; ++ i) {
				count[square[row][i]] ++;
			}
		}
		int ret, cnt = 0;
		for (int i = 1; i <= 16; ++ i) {
			if (count[i] == 2) {
				++ cnt;
				ret = i;
			}
		}
		cout << "Case #" << test << ": ";
		if (cnt == 1) {
			cout << ret << endl;
		} else if (cnt == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}
