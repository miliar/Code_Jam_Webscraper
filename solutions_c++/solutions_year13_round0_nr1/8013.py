#include <iostream>

using namespace std;

char A[4][4];
bool foundDot = false;

bool checkRow(int T)
{
	char c = ' ';

	for (int i = 0; i < 4; ++i)
	{
		bool rowTrue = true;
		c = ' ';

		for (int j = 0; j < 4; ++j)
		{
			if (c == '.')
				foundDot = true;

			if (A[i][j] == 'T')
				continue;


			if (c == ' ')
			{
				c = A[i][j];
				continue;
			}

			if ((c == '.') || (c != ' ' && c != A[i][j]))
			{
				rowTrue = false;
				break;
			}
		}

		if (rowTrue)
		{
			cout << "Case #" << T << ": " << c << " won" << endl;
			return true;
		}
	}

	return false;
}

bool checkCol(int T)
{
	char c = ' ';

	for (int i = 0; i < 4; ++i)
	{
		bool colTrue = true;
		c = ' ';

		for (int j = 0; j < 4; ++j)
		{
			if (c == '.')
				foundDot = true;

			if (A[j][i] == 'T')
				continue;

			if (c == ' ')
			{
				c = A[j][i];
				continue;
			}

			if ((c == '.') || (c != ' ' && c != A[j][i]))
			{
				colTrue = false;
				break;
			}
		}

		if (colTrue)
		{
			cout << "Case #" << T << ": " << c << " won" << endl;
			return true;
		}
	}

	return false;
}

bool checkDia1(int T)
{
	char c = ' ';
	bool colTrue = true;

	for (int i = 0; i < 4; ++i)
	{
		if (c == '.')
			foundDot = true;

		if (A[i][i] == 'T')
			continue;

		if (c == ' ')
		{
			c = A[i][i];
			continue;
		}

		if ((c == '.') || (c != ' ' && c != A[i][i]))
		{
			colTrue = false;
			break;
		}
	}

	if (colTrue)
	{
		cout << "Case #" << T << ": " << c << " won" << endl;
		return true;
	}

	return false;
}

bool checkDia2(int T)
{
	char c = ' ';
	bool colTrue = true;

	for (int i = 0; i < 4; ++i)
	{
		if (c == '.')
			foundDot = true;

		if (A[i][3 - i] == 'T')
			continue;

		if (c == ' ')
		{
			c = A[i][3 - i];
			continue;
		}

		if ((c == '.') || (c != ' ' && c != A[i][3 - i]))
		{
			colTrue = false;
			break;
		}
	}

	if (colTrue)
	{
		cout << "Case #" << T << ": " << c << " won" << endl;
		return true;
	}

	return false;
}

int main()
{
	int T = 0;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i)
	{
		foundDot = false;

		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
			{
				cin >> A[j][k];
			}
		}

		if (!checkRow(i+1))
		{
			if (!checkCol(i+1))
			{
				if (!checkDia1(i+1))
				{
					if (!checkDia2(i+1))
					{
						if (!foundDot)
						{
							cout << "Case #" << i+1 << ": " << "Draw" << endl;
						}
						else
						{
							cout << "Case #" << i+1 << ": " << "Game has not completed" << endl;
						}
					}
				}
			}
		}

		cin.get();
	}
		
	return 0;
}