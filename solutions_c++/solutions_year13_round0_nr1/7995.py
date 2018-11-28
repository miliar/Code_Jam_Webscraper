#include <iostream>

using namespace std;

int main()
{
	int n, totalVO, totalVX, totalHO, totalHX;
	char board[4][4];
	bool finished, done;

	cin >> n;

	for(int i = 0; i < n; i++)
	{
        done = false;
		finished = true;
		for(int j = 0; j < 4; j++)
		{
			for(int k = 0; k < 4; k++)
			{
				cin >> board[j][k];
			}
		}
		for(int j = 0; j < 4; j++)
		{
			totalVO = 0;
			totalVX = 0;
			totalHO = 0;
			totalHX = 0;
			for(int k = 0; k < 4; k++)
			{
				if(board[j][k] == 'O')
				{
					totalVO++;
				}
				else if(board[j][k] == 'X')
				{
					totalVX++;
				}
				else if(board[j][k] == 'T')
				{
					totalVO++;
					totalVX++;
				}
				else
				{
					finished = false;
				}
				if(board[k][j] == 'O')
				{
					totalHO++;
				}
				else if(board[k][j] == 'X')
				{
					totalHX++;
				}
				else if(board[k][j] == 'T')
				{
					totalHO++;
					totalHX++;
				}
			}
			if(totalVO == 4 || totalHO == 4)
			{
				cout << "Case #" << i+1 << ": O won" << "\n";
				done = true;
				break;
			}
			if(totalVX == 4 || totalHX == 4)
			{
				cout << "Case #" << i+1 << ": X won" << "\n";
				done = true;
				break;
			}
		}
		if(!done)
		{
		    if(finished)
            {
                cout << "Case #" << i+1 << ": Draw" << "\n";
                continue;
            }
            totalVO = 0;
            totalVX = 0;
            totalHO = 0;
            totalHX = 0;
            for(int j = 0; j < 4; j++)
            {
                if(board[j][j] == 'O')
                {
                    totalVO++;
                }
                else if(board[j][j] == 'X')
                {
                    totalVX++;
                }
                else if(board[j][j] == 'T')
                {
                    totalVO++;
                    totalVX++;
                }
                if(board[j][3-j] == 'O')
                {
                    totalHO++;
                }
                else if(board[j][3-j] == 'X')
                {
                    totalHX++;
                }
                else if(board[j][3-j] == 'T')
                {
                    totalHO++;
                    totalHX++;
                }
            }
            if(totalVO == 4 || totalHO == 4)
            {
                cout << "Case #" << i+1 << ": O won" << "\n";
                continue;
            }
            if(totalVX == 4 || totalHX == 4)
            {
                cout << "Case #" << i+1 << ": X won" << "\n";
                continue;
            }
            cout << "Case #" << i+1 << ": Game has not completed" << "\n";
		}
	}
	return 0;
}
