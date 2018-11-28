#include <cstdlib>
#include<iostream>
using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; ++i) {
		int  first_ans;
		int  sec_ans;
		int result;
		char *output = "Case #";
		bool found = false;
		int tmp;
		cin >> first_ans;
		int row_of_first_ans[4][4];
		int row_of_sec_ans[4][4];
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k)
				cin >> row_of_first_ans[j][k];
		}

		cin >> sec_ans;

		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k)
				cin >> row_of_sec_ans[j][k];
		}

		bool dup = false;
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				if (row_of_sec_ans[sec_ans - 1][j] == row_of_first_ans[first_ans - 1][k]) {
					if (!found){
						result = row_of_sec_ans[sec_ans - 1][j];
						found = true;
					}
					else {
						dup = true;
						cout << output << i << ": " << "Bad magician!" << endl;
						break;
					}

				}
			}
			if (dup) break;
		}

		if (!found) {
			cout << output << i << ": " << "Volunteer cheated!" << endl;
		}
		else if (!dup){
			cout << output << i << ": " << result << endl;
		}

	}
	return 0;
}