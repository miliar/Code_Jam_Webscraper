#include <iostream>
#include <cstdio>

using namespace std;
char matrix[4][4];

bool playerwon(char player) {

	int count1 = 0, count2 = 0;

	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if ((matrix[i][j] == player) || (matrix[i][j] == 'T'))
				count1++;
			if ((matrix[j][i] == player) || (matrix[j][i] == 'T')) {
				count2++;
			}
		}
		if (count1 == 4 || count2 == 4)
			return true;
		else
			count1 = count2 = 0;
	}
	count1 = count2 = 0;

	for (int i = 0; i < 4; ++i)
	{
		if ((matrix[i][i] == player) || (matrix[i][i] == 'T'))
			count1++;
		if ((matrix[3 - i][i] == player) || (matrix[3 - i][i] == 'T'))
			count2++;
	}
	return (count1 == 4 || count2 == 4);
}

bool matrixcomplete() {

	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (matrix[i][j] == '.')
				return false;
		}
	}
	return true;
}

int main() {

	int t;
	bool x = 0, o = 0;
	cin >> t;

	for (int cas = 1; cas <= t; ++cas)
	{	
		x = o = 0;
		for (int i = 0; i < 4; ++i)
		{
			cin >> matrix[i];
		}
		
		if (playerwon('X'))
			x = 1;
		if (playerwon('O'))
			o = 1;

		printf("Case #%d: ", cas);
		if (x && o)
			cout << "Draw\n";
		else if (x)
			cout << "X won\n";
		else if (o)
			cout << "O won\n";
		else if (matrixcomplete())
			cout << "Draw\n";
		else 
			cout << "Game has not completed\n";
	}
}
