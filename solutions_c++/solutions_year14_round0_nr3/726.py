#include <iostream>
using namespace std;
char board[51][51];

void display(int r, int c, int m)
{
	for (int yloop = 0; yloop < r; yloop++, cout << endl)
		for (int xloop = 0; xloop < c; xloop++)
			cout << board[yloop][xloop];
}

int cal(int r, int c, int m)
{
	if (c == 1 || r == 1)
	{
		board[0][0] = 'c';
		for (int rloop = r - 1; rloop >= 0 && m > 0; rloop--)
			for (int cloop = c - 1; cloop >= 0 && m > 0; cloop--)
			{
				board[rloop][cloop] = '*';
				m--;
			}
		return 1;
	}

	int empty = r * c - m;
	int new_m = m, new_r = r, new_c = c;
	for (int rloop = 2; rloop <= r; rloop++)
		for (int cloop = 2; cloop <= c; cloop++)
		{
			int tmp_m = rloop * cloop - empty;
			if (tmp_m >= 0 && tmp_m < new_m)
			{
				new_m = tmp_m;
				new_r = rloop;
				new_c = cloop;
			}
		}
	for (int rloop = 0; rloop < r; rloop++)
		for (int cloop = 0; cloop < c; cloop++)
			if (rloop >= new_r || cloop >= new_c) board[rloop][cloop] = '*';

	for (int rloop = new_r - 1; rloop >= 2 && new_m > 0; rloop--)
		for (int cloop = new_c - 1; cloop >= 2 && new_m > 0; cloop--)
		{
			board[rloop][cloop] = '*';
			new_m--;
		}

	if ( r*c == m + 1)
	{
		memset(board, '*', sizeof(char)* 51 * 51);
		board[0][0] = 'c';
		return 1;
	}
	else if (new_m == 0)
	{
		board[0][0] = 'c';
		return 1;
	}
	else if (new_m > 0) return -1;
}

int main()
{
	int t; cin >> t;
	for (int loop = 1; loop <= t; loop++)
	{
		memset(board, '.', sizeof(char)* 51 * 51);
		int r, c, m; cin >> r >> c >> m;
		cout << "Case #" << loop << ":" << endl;
		if (cal(r, c, m) == -1) cout << "Impossible" << endl;
		else
			display(r, c, m);
	}
}