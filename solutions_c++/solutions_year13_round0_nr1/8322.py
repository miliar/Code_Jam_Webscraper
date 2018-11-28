
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

bool check(std::vector<string> &board, char ele, bool visit[4][4]){
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
			{
				if (!visit[i][j] && board[i][j] == ele)
				{
					/* code */
					int m;

					for(m = 0; m < 4; ++m){
						visit[i][m] = true;
						if(board[i][m] == ele || board[i][m] == 'T'){
							continue;
						}
						else{
							break;
						}
					}
					if (m == 4)
					{
						return true;
					}
					for(m = 0; m < 4; ++m){
						visit[m][j] = true;
						if(board[m][j] == ele || board[m][j] == 'T'){
							continue;
						}
						else{
							break;
						}
					}
					if (m == 4)
					{
						return true;
					}
					if (i == j)
					{
						for(m = 0; m < 4; ++m){
							visit[m][m] = true;
							if(board[m][m] == ele || board[m][m] == 'T'){
								continue;
							}
							else{
								break;
							}
						}
						if (m == 4)
						{
							return true;
						}
					}
					if (i + j == 3)
					{
						for(m = 0; m < 4; ++m){
							visit[m][3-m] = true;
							if(board[m][3-m] == ele || board[m][3-m] == 'T'){
								continue;
							}
							else{
								break;
							}
						}
						if (m == 4)
						{
							return true;
						}
					}
				}
			}	
	}
	return false;
}

void check(std::vector<string> &board, int t){
	bool visit[4][4] = {false};
	bool x_win = false;
	bool o_win = false;
	x_win = check(board, 'X', visit);
	if (x_win)
	{
		printf("Case #%d: X won\n", t);
		return;
	}
	o_win = check(board, 'O', visit);
	if (o_win)
	{
		printf("Case #%d: O won\n", t);
		return;
	}
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (board[i][j] == '.')
			{
				printf("Case #%d: Game has not completed\n", t);
				return;
			}
		}
	}
	printf("Case #%d: Draw\n", t);
}

int main()
{
    int t;
    ifstream ios("A-small-attempt1.in");
	ios>>t;
	vector<string> board(4);
	for (int p = 1; p <= t; ++p){
		ios>>board[0];
		ios>>board[1];
		ios>>board[2];
		ios>>board[3];
		check(board, p);
	}
    ios.close();
    return 0;
}