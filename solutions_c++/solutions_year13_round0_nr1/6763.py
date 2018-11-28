#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

char xWinT[4] = {'T', 'X', 'X', 'X'};
char xWin[4] = {'X', 'X', 'X', 'X'};
char oWinT[4] = {'O', 'O', 'O', 'T'};
char oWin[4] = {'O', 'O', 'O', 'O'};


int judge(char ticMap[4][4])
{
	int i, j, k;
	char newMap[4];	
	int ret = -1;
	bool hasEmpty = false;
	for (i = 0; i < 4; ++i)
	{
		for (j = 0; j < 4; ++j)
		{
			newMap[j] = ticMap[i][j];
			if (newMap[j] == '.')
			{
				hasEmpty = true;
			}
		}
		sort(newMap, newMap + 4);						
		if (memcmp(newMap, xWinT, sizeof(char) * 4) == 0
			|| memcmp(newMap, xWin, sizeof(char) * 4) == 0)
		{
			return 0;
		}
		else if (memcmp(newMap, oWinT, sizeof(char) * 4) == 0
			|| memcmp(newMap, oWin, sizeof(char) * 4) == 0)
		{
			return 1;
		}
	}

	for (i = 0; i < 4; ++i)
	{
		for (j = 0; j < 4; ++j)
		{
			newMap[j] = ticMap[j][i];
		}
		sort(newMap, newMap + 4);
		if (memcmp(newMap, xWinT, sizeof(char) * 4) == 0
			|| memcmp(newMap, xWin, sizeof(char) * 4) == 0)
		{
			return 0;
		}
		else if (memcmp(newMap, oWinT, sizeof(char) * 4) == 0
			|| memcmp(newMap, oWin, sizeof(char) * 4) == 0)
		{
			return 1;
		}
	}
	
	for (i = 0; i < 4; ++i)
	{
		newMap[i] = ticMap[i][i];		
	}
	sort(newMap, newMap + 4);
	if (memcmp(newMap, xWinT, sizeof(char) * 4) == 0
		|| memcmp(newMap, xWin, sizeof(char) * 4) == 0)
	{
		return 0;
	}
	else if (memcmp(newMap, oWinT, sizeof(char) * 4) == 0
		|| memcmp(newMap, oWin, sizeof(char) * 4) == 0)
	{
		return 1;
	}

	for (i = 0; i < 4; ++i)
	{
		newMap[i] = ticMap[i][3 - i];		
	}
	sort(newMap, newMap + 4);
	if (memcmp(newMap, xWinT, sizeof(char) * 4) == 0
		|| memcmp(newMap, xWin, sizeof(char) * 4) == 0)
	{
		return 0;
	}
	else if (memcmp(newMap, oWinT, sizeof(char) * 4) == 0
		|| memcmp(newMap, oWin, sizeof(char) * 4) == 0)
	{
		return 1;
	}
	
	if (hasEmpty)
	{
		return 3;
	}
	return 2;

}

int main()
{
	// ifstream ifs("in.txt");
	// ifstream ifs("A-small-attempt0.in");
	ifstream ifs("A-large.in");
	ofstream ofs("out.txt");
	cin.rdbuf(ifs.rdbuf());
	cout.rdbuf(ofs.rdbuf());
	string res[] = {"X won", "O won", "Draw" ,"Game has not completed"};
	int T;
	cin >> T;
	int i, j, k;
	char ticMap[4][4];
	for (i = 1; i <= T; ++i)
	{
		for (j = 0; j < 4; ++j)
		{
			for (k = 0; k < 4; ++k)
			{
				cin >> ticMap[j][k];				
			}			
		}
		// judge(ticMap);
		cout << "Case #" << i << ": " << res[judge(ticMap)] << endl;
	}
	ofs.close();
	ifs.close();
	return 0;
}