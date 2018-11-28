#include <iostream>
#include <cstring>
using namespace std;

int main()
{
	freopen ("test.in", "a+", stdin);
	freopen ("test.out", "w", stdout);

	int tests;
	char arr[4][4];
	char shit[5];
	cin >> tests;
	for (int t = 0; t < tests; ++t)
	{
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> arr[i][j];
		gets(shit);

		int x, o, res = 5;
		bool dot = false;

		//check rows
		for (int i = 0; i < 4; ++i)
		{
			x = 0;
			o = 0;
			for (int j = 0; j < 4; ++j)
			{
				if (arr[j][i] == 'X')
					++x;
				if (arr[j][i] == 'O')
					++o;
				if (arr[j][i] == 'T')
				{
					++x;
					++o;
				}
				if (arr[j][i] == '.')
					dot = true;
			}
			if (x == 4)
			{
				res = 0;
				break;
			}
			if (o == 4)
			{
				res = 1;
				break;
			}
		}
		if (res == 0)
		{
			cout << "Case #" << t + 1 << ": X won" << endl;
			continue;
		}
		if (res == 1)
		{
			cout << "Case #" << t + 1 << ": O won" << endl;
			continue;
		}

		//check cols
		for (int i = 0; i < 4; ++i)
		{
			x = 0;
			o = 0;
			for (int j = 0; j < 4; ++j)
			{
				if (arr[i][j] == 'X')
					++x;
				if (arr[i][j] == 'O')
					++o;
				if (arr[i][j] == 'T')
				{
					++x;
					++o;
				}
				if (arr[i][j] == '.')
					dot = true;
			}
			if (x == 4)
			{
				res = 0;
				break;
			}
			if (o == 4)
			{
				res = 1;
				break;
			}
		}
		if (res == 0)
		{
			cout << "Case #" << t + 1 << ": X won" << endl;
			continue;
		}
		if (res == 1)
		{
			cout << "Case #" << t + 1 << ": O won" << endl;
			continue;
		}


		//check first diagonal
		x = 0;
		o = 0;
		for (int i = 0; i < 4; ++i)
		{
			if (arr[i][i] == 'X')
				++x;
			if (arr[i][i] == 'O')
				++o;
			if (arr[i][i] == 'T')
			{
				++x;
				++o;
			}
		}
		if (x == 4)
		{
			cout << "Case #" << t + 1 << ": X won" << endl;
			continue;
		}
		if (o == 4)
		{
			cout << "Case #" << t + 1 << ": O won" << endl;
			continue;
		}

		//check second diagonal
		x = 0;
		o = 0;
		for (int i = 0; i < 4; ++i)
		{
			if (arr[i][3 - i] == 'X')
				++x;
			if (arr[i][3 - i] == 'O')
				++o;
			if (arr[i][3 - i] == 'T')
			{
				++x;
				++o;
			}
		}
		if (x == 4)
		{
			cout << "Case #" << t + 1 << ": X won" << endl;
			continue;
		}
		if (o == 4)
		{
			cout << "Case #" << t + 1 << ": O won" << endl;
			continue;
		}

		if (dot)
		{
			cout << "Case #" << t + 1 << ": Game has not completed" << endl;
		}
		else
		{
			cout << "Case #" << t + 1 << ": Draw" << endl;
		}
	}
	return 0;
}