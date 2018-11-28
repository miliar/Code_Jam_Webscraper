#include <iostream>
#include <vector>

using namespace std;

int guessCard(int row1, vector<vector<int> >& grid1, int row2, vector<vector<int> >& grid2)
{
	int card = -2;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (grid1[row1-1][i] == grid2[row2-1][j])
			{
				if (card != -2)
					return -1;
				card = grid1[row1-1][i];
			}
		}
	}
	
	return card;
}

void loadInput(int& row, vector<vector<int> >& grid)
{
	cin >> row;
	for (int r = 0; r < 4; ++r)
		for (int c = 0; c < 4; ++c)
			cin >> grid[r][c];
}

int main()
{
	int T,row1,row2;
	vector<vector<int> > grid1 = vector<vector<int> >(4, vector<int>(4));
	vector<vector<int> > grid2 = vector<vector<int> >(4, vector<int>(4));
	cin >> T;
	for (int t = 0; t < T; ++t)
	{	
		loadInput(row1, grid1);
		loadInput(row2, grid2);
		int result = guessCard(row1, grid1, row2, grid2);

		printf("Case #%d: ", (t+1));
		if (result == -1)
			cout << "Bad magician!" << endl;
		else if (result == -2)
			cout << "Volunteer cheated!" << endl;
		else
			cout << result << endl;
	}
	
	return 0;
}