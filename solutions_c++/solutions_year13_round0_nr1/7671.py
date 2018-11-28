//A - Tic-Tac-Toe-Tomek

#include<iostream>
#include<string>
using namespace std;

bool won(char grid[4][4], char in)
{
	for(int i = 0; i < 4; i++)
	{
		bool flag[2] = {1, 1};
		for(int j = 0; j < 4; j++)
		{
			flag[0] &= (grid[i][j] == in || grid[i][j] == 'T');
			flag[1] &= (grid[j][i] == in || grid[j][i] == 'T');
		}
		if(flag[0]||flag[1])
			return 1;
	}
	bool flag[2] = {1, 1};
	for(int i = 0; i < 4; i++)
	{
		flag[0] &= (grid[i][i] == in || grid[i][i] == 'T');
		flag[1] &= (grid[i][3-i] == in || grid[i][3-i] == 'T');
	}
	return flag[0] || flag[1];
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int T; cin >> T;
	for(int tt = 1; tt<=T; tt++)
	{
		char grid[4][4];
		int c = 0;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
			{
				cin >> grid[i][j];
				c+=(grid[i][j]=='.');
			}
		bool flag[2] = {won(grid, 'X'), won(grid, 'O')};
		cout << "Case #" << tt << ": ";
		if(flag[0]) cout << "X won\n";
		else if(flag[1]) cout << "O won\n";
		else if(c==0) cout << "Draw\n";
		else cout << "Game has not completed\n";
	}

	return 0;
}
