#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int ans1, ans2;
		int board1[4][4];
		int board2[4][4];
		vector<int> board1Pos;
		vector<int> board2Pos;
		cin >> ans1;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> board1[j][k];
				
		cin >> ans2;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				cin >> board2[j][k];
		
		for (int j = 0; j < 4; j++)
		{
			board1Pos.push_back(board1[ans1-1][j]);
			board2Pos.push_back(board2[ans2-1][j]);
		}
		
		int matching = 0;
		int cand;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				if (board1Pos[j] == board2Pos[k])
				{
					matching++;
					cand = board1Pos[j];
				}
		
		if (matching == 1)
			cout << "Case #" << i << ": " << cand << endl;
		else if (matching < 1)
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		else
			cout << "Case #" << i << ": Bad magician!" << endl;
	}
	return 0;
}
