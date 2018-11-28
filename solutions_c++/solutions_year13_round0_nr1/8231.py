#include <iostream>
#include <string>
using namespace std;
#define rep(i, n) REP(i, 0, n)
#define REP(i, x, n) for(int i=x; i<n; i++)

char board[4][4];

int r(int y, int x, char tar)
{
	int cnt = 0;
	REP(i, x, x+3) cnt += tar == board[y][i];
	return cnt == 3;
}

int c(int x, int y, char tar)
{
	int cnt = 0;
	REP(i, y, y+3) cnt += tar == board[i][x];
	return cnt == 3;
}

int l(int x, int y, int tar)
{
	int cnt = 0;
	for(int i = y, j = x; i < y+3; i++, (x < 2 ? j++ : j--)) cnt += tar == board[i][j];
	return cnt == 3;
}

int main()
{
	int N;
	cin >> N;

	rep(i, N)
	{
		if(i != 0){ string tmp; getline(cin, tmp); }
		
		rep(j, 4) rep(k, 4) cin >> board[j][k];
		
		string ans = "Draw";

		rep(j, 4) rep(k, 4) if(board[j][k] == '.') ans = "Game has not completed";
		
		rep(j, 4)
		{
			if((r(j, 0, 'X') && (board[j][3] == 'X' || board[j][3] == 'T')) ||
				 (r(j, 1, 'X') && (board[j][0] == 'X' || board[j][0] == 'T')))
				ans = "X won";

			if((r(j, 0, 'O') && (board[j][3] == 'O' || board[j][3] == 'T')) ||
				 (r(j, 1, 'O') && (board[j][0] == 'O' || board[j][0] == 'T')))
				ans = "O won";

			if((c(j, 0, 'X') && (board[3][j] == 'X' || board[3][j] == 'T')) ||
				 (c(j, 1, 'X') && (board[0][j] == 'X' || board[0][j] == 'T')))
				ans = "X won";

			if((c(j, 0, 'O') && (board[3][j] == 'O' || board[3][j] == 'T')) ||
				 (c(j, 1, 'O') && (board[0][j] == 'O' || board[0][j] == 'T')))
				ans = "O won";
		}

		if((l(0, 0, 'X') && (board[3][3] == 'X' || board[3][3] == 'T')) ||
			 (l(1, 1, 'X') && (board[0][0] == 'X' || board[0][0] == 'T')))
			ans = "X won";

		if((l(0, 0, 'O') && (board[3][3] == 'O' || board[3][3] == 'T')) ||
			 (l(1, 1, 'O') && (board[0][0] == 'O' || board[0][0] == 'T')))
			ans = "O won";

		if((l(3, 0, 'X') && (board[3][0] == 'X' || board[3][0] == 'T')) ||
			 (l(2, 1, 'X') && (board[0][3] == 'X' || board[0][3] == 'T')))
			ans = "X won";

		if((l(3, 0, 'O') && (board[3][0] == 'O' || board[3][0] == 'T')) ||
			 (l(2, 1, 'O') && (board[0][3] == 'O' || board[0][3] == 'T')))
			ans = "O won";

		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}
