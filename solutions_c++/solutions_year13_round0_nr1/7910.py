#include<iostream>
#include<string>
#include<vector>
using namespace std;

bool checkWin (char c, vector <string> &b)
{
	int cnt1 = 0, cnt2 = 0, cnt3 = 0, cnt4 = 0;

	for (int i=0; i<4; i++)
	{
		cnt3 += (b[i][i] == c || b[i][i] == 'T');
		cnt4 += (b[i][4-i-1] == c || b[i][4-i-1] == 'T');
		cnt1 = 0;
		cnt2 = 0;
		for (int j=0; j<4; j++)
		{
			cnt1 += (b[i][j]== c || b[i][j] == 'T');
			cnt2 += (b[j][i] == c || b[j][i] == 'T');
		}
		if (cnt1 == 4 || cnt2 == 4)
			return true;
	}
	if (cnt3 == 4 || cnt4 == 4)
		return true;

	else
		return false;
	
}

int main ()
{
	//freopen ("in.txt", "r", stdin);
	//freopen ("out.txt", "w", stdout);
	int T;
	cin >> T;

	vector<string> board(4);

	for (int cases = 1; cases <=T; cases++)
	{
		for (int i=0; i<4; i++)
			cin >> board[i];

		cout << "Case #" << cases <<": ";
		if (checkWin('X', board))
			cout << "X won\n";
		else if (checkWin('O',board ))
			cout << "O won\n";
		else 
		{
			int cnt = 0;
			for (int i=0; i<4; i++)
				for (int j=0; j<4; j++)
					cnt += board[i][j] == '.';
			if (cnt > 0)
				cout << "Game has not completed\n";
			else
				cout << "Draw\n";
		}
	}

	return 0;
}