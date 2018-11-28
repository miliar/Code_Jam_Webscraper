#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

using namespace std;
char board[4][4];

#define ROW_WIN(ROW, TROW, COUNT)	((COUNT == 4) || ((COUNT == 3) && (TROW == ROW)))
#define COL_WIN(COL, TCOL, COUNT)	((COUNT == 4) || ((COUNT == 3) && (TCOL == COL)))

#define T_IN_DIAG(TROW, TCOL)		((TROW == TCOL) || (TROW + TCOL == 3))
#define DIAG_WIN(TROW, TCOL, COUNT)	((COUNT == 4) || ((COUNT == 3) && (T_IN_DIAG(TROW, TCOL))))

void print_status(int trow, int tcol)
{
	int	row[4][2];
	int	col[4][2];
	int	ldiag[2] = {0, 0};
	int	rdiag[2] = {0, 0};
	int	empty_cnt = 0;

	memset(row, 0, sizeof(int) * 4 * 2);
	memset(col, 0, sizeof(int) * 4 * 2);
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (board[i][j] == 'X')
			{
				row[i][0]++;
				col[j][0]++;
			} else if (board[i][j] == 'O')
			{
				row[i][1]++;
				col[j][1]++;
			}
			empty_cnt += (board[i][j] == '.');
		}
		ldiag[0] += (board[i][i] == 'X');
		ldiag[1] += (board[i][i] == 'O');
		rdiag[0] += (board[i][4 - i - 1] == 'X');
		rdiag[1] += (board[i][4 - i - 1] == 'O');
	}
	if (DIAG_WIN(trow, tcol, ldiag[0]) || DIAG_WIN(trow, tcol, rdiag[0]))
	{
		cout << "X won" << endl;
		return;
	} else if (DIAG_WIN(trow, tcol, ldiag[1]) || DIAG_WIN(trow, tcol, rdiag[1]))
	{
		cout << "O won" << endl;
		return;
	}
	for (int i = 0; i < 4; i++)
	{
		if (ROW_WIN(i, trow, row[i][0]) || COL_WIN(i, tcol, col[i][0]))
		{
			cout << "X won" << endl;
			return;
		} else if (ROW_WIN(i, trow, row[i][1]) || COL_WIN(i, tcol, col[i][1]))
		{
			cout << "O won" << endl;
			return;
		}
	}
	if (empty_cnt > 0)
	{
		cout << "Game has not completed" << endl;
		return;
	}
	cout << "Draw" << endl;
	return;

}
int main()
{
	int	t;
	char	c;

	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		int trow, tcol;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				cin >> board[i][j];
				if (board[i][j] == 'T')
				{
					trow = i;
					tcol = j;
				}
			}
		cout << "Case #" << tt << ": ";
		print_status(trow, tcol);
	}
}
