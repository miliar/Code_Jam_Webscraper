#if 1

#include <iostream>
#include <math.h>
using namespace std;
#define ROWS 4
#define COLS 4

int main ()
{
	bool test(const int caseNum, const int sum);

	int cases;

	cin >> cases;

	for (int i = 0; i < cases; ++i)
	{
		int horizontal[ROWS] = {0};
		int vertical[COLS] = {0};
		int mainDiagonal = 0;
		int otherDiagonal = 0;
		
		for (int j = 0; j < ROWS*COLS; ++j)
		{
			char cell;
			cin >> cell;

			int numeric_val = 0;
			switch (cell)
			{
			case 'X' : numeric_val = -1;   break;
			case 'T' : numeric_val = 0;    break;
			case 'O' : numeric_val = 1;    break;
			case '.' : numeric_val = -9999; break;
			}

			int row = j/4;
			int col = j%4;

			horizontal[row] += numeric_val;
			vertical[col] += numeric_val;

			if (row == col)
			{
				mainDiagonal += numeric_val;
			}
			else if (3 == row + col)
			{
				otherDiagonal += numeric_val;
			}
		}

		int cn = i+1;

		if (test (i+1, mainDiagonal) || test (i+1, otherDiagonal) ||
			test (i+1, horizontal[0]) || test (i+1, horizontal[1]) || test (i+1, horizontal[2]) || test (i+1, horizontal[3]) ||
			test (i+1, vertical[0]) || test (i+1, vertical[1]) || test (i+1, vertical[2])  || test (i+1, vertical[3]))
		{
			continue;
		}

		// Either draw or Game not completed, check if any cell not filled yet
		if (horizontal[0] < -4 || horizontal[1] < -4 || horizontal[2] < -4 || horizontal[3] < -4)
		{
			cout << "Case #" << i+1 << ": Game has not completed" << endl;
			continue;
		}

		cout << "Case #" << i+1 << ": Draw" << endl;
	}

	return 0;
}

bool test(const int caseNum, const int sum)
{
	if (3 == abs(sum) || 4 == abs(sum))
	{
		cout << "Case #" << caseNum << ": " << ((sum < 0) ? "X" : "O") << " won" << endl;

		return true;
	}

	return false;
}
#endif
