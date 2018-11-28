#include <iostream>
#include <vector>
using namespace std;
int board[2][4][4], row[2];
int row1, row2;
int main()
{
	int T;
	cin >> T;
	for (int cases = 1; cases <= T; cases++)
	{
		for (int p = 0; p < 2; p++)
		{
			cin >> row[p];
			row[p]--;
			for (int i = 0; i < 4; i++)
				for (int j = 0; j < 4; j++)
					cin >> board[p][i][j];
		}
		vector<int> sols;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (board[0][row[0]][i] == board[1][row[1]][j])
					sols.push_back(board[0][row[0]][i]);
		if (sols.size() == 1) cout << "Case #" << cases << ": " << sols[0] << endl;
		else if (sols.size() > 1) cout << "Case #" << cases << ": Bad magician!" << endl;
		else cout << "Case #" << cases << ": Volunteer cheated!" << endl;
	}
	return 0;
}