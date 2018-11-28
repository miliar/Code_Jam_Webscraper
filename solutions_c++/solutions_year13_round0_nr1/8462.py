
#include <iostream>
#include <string>
#include <vector>
#include <Windows.h>

using namespace std;

enum
{
	RESULT_X_WON,
	RESULT_O_WON,
	RESULT_DRAW,
	RESULT_NOT_COMPLETED,
	RESULT_MAX
};

void Tic_Tac_Toe_Tomek(void)
{
	vector<int> result;
	int count = 0;
	cin >> count;

	for (int i = 0; i < count; ++i)
	{
		bool hasDot = false;
		bool isOver = false;
		char winner = 'T';
		char letters[4][4];
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> letters[j][k];
			}
		}
		for (int j = 0; j < 4; ++j)
		{
			// row
			char tmp = letters[j][0];
			if (tmp == '.')
			{
				hasDot = true;
				continue;
			}
			int k;
			for (k = 1; k < 4; ++k)
			{
				if (letters[j][k] == '.')
				{
					hasDot = true;
					break;
				}
				if (tmp == 'T')
				{
					tmp = letters[j][k];
				}
				else if (letters[j][k] == 'T')
				{
					continue;
				}
				else if (tmp != letters[j][k])
				{
					break;
				}
			}
			if (k == 4)
			{
				isOver = true;
				winner = tmp;
				break;
			}
			// column
			tmp = letters[0][j];
			if (tmp == '.')
			{
				hasDot = true;
				continue;
			}
			for (k = 1; k < 4; ++k)
			{
				if (letters[k][j] == '.')
				{
					hasDot = true;
					break;
				}
				if (tmp == 'T')
				{
					tmp = letters[k][j];
				}
				else if (letters[k][j] == 'T')
				{
					continue;
				}
				else if (tmp != letters[k][j])
				{
					break;
				}
			}
			if (k == 4)
			{
				isOver = true;
				winner = tmp;
				break;
			}
		}
		if (!isOver)
		{
			// diagonal
			char tmp = letters[0][0];
			if (tmp == '.')
			{
				hasDot = true;
			}
			int k;
			for (k = 1; k < 4; ++k)
			{
				if (letters[k][k] == '.')
				{
					hasDot = true;
					break;
				}
				if (tmp == 'T')
				{
					tmp = letters[k][k];
				}
				else if (letters[k][k] == 'T')
				{
					continue;
				}
				else if (tmp != letters[k][k])
				{
					break;
				}
			}
			if (k == 4)
			{
				isOver = true;
				winner = tmp;
			}
			tmp = letters[0][3];
			if (tmp == '.')
			{
				hasDot = true;
			}
			for (k = 1; k < 4; ++k)
			{
				if (letters[k][3-k] == '.')
				{
					hasDot = true;
					break;
				}
				if (tmp == 'T')
				{
					tmp = letters[k][3-k];
				}
				else if (letters[k][3-k] == 'T')
				{
					continue;
				}
				else if (tmp != letters[k][3-k])
				{
					break;
				}
			}
			if (k == 4)
			{
				isOver = true;
				winner = tmp;
			}
		}
		if (isOver)
		{
			if (winner == 'X')
			{
				result.push_back(RESULT_X_WON);
			}
			else if (winner == 'O')
			{
				result.push_back(RESULT_O_WON);
			}
		}
		else if (hasDot)
		{
			result.push_back(RESULT_NOT_COMPLETED);
		}
		else
		{
			result.push_back(RESULT_DRAW);
		}
	}

	FILE *file = fopen("1.txt", "wb");
	
	vector<int>::iterator it = result.begin();
	for (int i = 0; it != result.end(); ++it, ++i)
	{
		char str[64];
		sprintf(str, "Case #%d: ", i + 1);
		fwrite(str, strlen(str), 1, file);
		//cout << "Case #" << i + 1 << ": ";
		switch (*it)
		{
		case RESULT_X_WON:
			sprintf(str, "X won\n");
			//cout << "X won\x0a";
			break;
		case RESULT_O_WON:
			sprintf(str, "O won\n");
			//cout << "O won\x0a";
			break;
		case RESULT_NOT_COMPLETED:
			sprintf(str, "Game has not completed\n");
			//cout << "Game has not completed\x0a";
			break;
		case RESULT_DRAW:
			sprintf(str, "Draw\n");
			//cout << "Draw\x0a";
			break;
		}
		fwrite(str, strlen(str), 1, file);
	}
	fclose(file);
}

int main(void)
{
	Tic_Tac_Toe_Tomek();

// 	system("pause");

	return 0;
}