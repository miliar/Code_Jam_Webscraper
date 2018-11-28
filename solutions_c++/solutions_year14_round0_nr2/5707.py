#include <iostream>

using namespace std;

int main ()
{
	int T = 0;
	int row_num1 = 0, row_num2 = 0;
	int grid1 [4][4], grid2 [4][4];
	int solve_kol = 0, solve = 0;
	
	cin >> T;
		
	for (int t = 0; t < T; t ++)
	{
		solve = 0;
		solve_kol = 0;
		
		cin >> row_num1;
		for (int i = 0; i < 4; i ++)
		{
			cin >> grid1 [i][0] >> grid1 [i][1] >> grid1 [i][2] >> grid1 [i][3];
		}
		cin >> row_num2;
		for (int i = 0; i < 4; i ++)
		{
			cin >> grid2 [i][0] >> grid2 [i][1] >> grid2 [i][2] >> grid2 [i][3];
		}

		for (int i = 0; i < 4; i ++)
		{
			for (int j = 0; j < 4; j ++)
			{
				if ( grid1 [row_num1-1][i] == grid2 [row_num2-1][j] )
				{
					solve = grid1 [row_num1-1][i];
					solve_kol ++;
				}
			}
		}
		
		if ( solve_kol == 0 )
		{
			cout << "Case #" << t+1 << ": Volunteer cheated!" << endl;
		}
		else if ( solve_kol == 1 )
		{
			cout << "Case #" << t+1 << ": " << solve << endl;
		}
		else if ( solve_kol > 1 )
		{
			cout << "Case #" << t+1 << ": Bad magician!" << endl;
		}
			
	}

	return 0;
}
