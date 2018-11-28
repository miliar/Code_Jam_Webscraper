#include <iostream>
#include <vector>

using namespace std;

int main() {
	int T;
	int select1, select2;
	int board1[4][4], board2[4][4];
	vector<int> redundant_values;

	cin >> T;

	for (int t = 1; t <= T; t++) {

		redundant_values.clear();		

		// input
		cin >> select1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> board1[i][j];
		cin >> select2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> board2[i][j];

		// solve
		select1--;
		select2--;
		for (int i = 0; i < 4; i++) {
			for (int k = 0; k < 4; k++) {
				if (board1[select1][i] == board2[select2][k])
					redundant_values.push_back(board1[select1][i]);
			}
		}

		// output
		cout << "Case #" << t << ": ";
		if (redundant_values.size() == 1)
			cout << redundant_values[0];
		else if (redundant_values.size() > 1)
			cout << "Bad magician!";
		else
			cout << "Volunteer cheated!";
		cout << "\n";
	}

	

	return 0;
}