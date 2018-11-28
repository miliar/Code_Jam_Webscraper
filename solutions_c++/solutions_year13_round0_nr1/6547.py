# include <fstream>
# include <iostream>
# include <string>
# include <vector>
# include <math.h>
# include <algorithm>
# include <string.h>
# include <stack>
# include <queue>
# include <sstream>
# include <set>
# include <map>
# include <assert.h>
using namespace std;

char field[4][4];
bool hasWon(char ch)
{
	for (int i = 0; i < 4; i++)
	{
		int t = 0;
		int num = 0;
		for (int j = 0; j < 4; j++)
			if (field[i][j] == 'T')
				t++;
			else
				if (field[i][j] == ch)
					num++;
		if (num == 4 || t == 1 && num == 3)
			return true;
	}

	for (int j = 0; j < 4; j++)
	{
		int t = 0;
		int num = 0;
		for (int i = 0; i < 4; i++)
			if (field[i][j] == 'T')
				t++;
			else
				if (field[i][j] == ch)
					num++;
		if (num == 4 || t == 1 && num == 3)
			return true;
	}

	int t = 0, num = 0;
	for (int i = 0; i < 4; i++)
	{
		if (field[i][i] == 'T')
			t++;
		else
			if (field[i][i] == ch)
				num++;
		if (num == 4 || t == 1 && num == 3)
			return true;
	}

	t = 0; num = 0;
	for (int i = 0, j = 3; i < 4; i++, j--)
	{
		if (field[i][j] == 'T')
			t++;
		else
			if (field[i][j] == ch)
				num++;
		if (num == 4 || t == 1 && num == 3)
			return true;
	}

	return false;
}

int main()
{
    //ios_base::sync_with_stdio(false);
    ifstream cin ("input.txt");
    ofstream cout ("output.txt");

	int t;
	cin >> t;
	for (int test = 0; test < t; test++)
	{
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> field[i][j];

		int dotNum = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (field[i][j] == '.')
					dotNum++;

		cout << "Case #" << test + 1 << ": ";

		if (hasWon('X'))
			cout << "X won";
		else
			if (hasWon('O'))
				cout << "O won";
			else
				if (dotNum == 0)
					cout << "Draw";
				else
					cout << "Game has not completed";

		cout << endl;
	}
    
    //system("pause");
    return 0;
}
