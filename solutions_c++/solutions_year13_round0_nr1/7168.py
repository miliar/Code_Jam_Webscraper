#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	string s[4];
	cin >> t;
	for (int test = 1; test <= t; test++) {
		for (int i = 0; i < 4; i++)
			cin >> s[i];

		int colO[4] = {0}, colX[4] = {0}, rowO[4] = {0}, rowX[4] = {0};
		// -1 nothing
		// 0  О
		// 1  X
		int state = -1;
		bool completed = true;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if ((s[i][j] == 'T') || (s[i][j] == 'O')) {
					colO[j]++;
					rowO[i]++;
				}
				if ((s[i][j] == 'T') || (s[i][j] == 'X')) {
					colX[j]++;
					rowX[i]++;
				}
				if (s[i][j] == '.')
					completed = false;
			}
		}
		for (int i = 0; i < 4; i++) {
			if ((rowO[i] == 4) || (colO[i] == 4)) {
				state = 0;
				break;
			}
			if ((rowX[i] == 4) || (colX[i] == 4)) {
				state = 1;
				break;
			}
		}
		int diagO_1 = 0, diagX_1 = 0;
		for (int i = 0; i < 4; i++) {
			if ((s[i][i] == 'T') || (s[i][i] == 'O')) {
				diagO_1++;
			}
			if ((s[i][i] == 'T') || (s[i][i] == 'X')) {
				diagX_1++;
			}	
		}
		int diagO_2 = 0, diagX_2 = 0;
		for (int i = 0; i < 4; i++) {
			if ((s[i][3-i] == 'T') || (s[i][3-i] == 'O')) {
				diagO_2++;
			}
			if ((s[i][3-i] == 'T') || (s[i][3-i] == 'X')) {
				diagX_2++;
			}	
		}

		if ((diagO_1 == 4) || (diagO_2 == 4)) {
				state = 0;
		}
		if ((diagX_1 == 4) || (diagX_2 == 4)) {
			state = 1;
		}

		cout << "Case #" << test << ": ";
		if (state == 1)
			cout << "X won";
		else if (state == 0)
			cout << "O won";
		else if (completed == true)
			cout << "Draw";
		else
			cout << "Game has not completed";
		cout << endl;
	}

	return 0;
}

