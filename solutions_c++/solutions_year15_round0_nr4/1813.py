// Google Code Jam 2015
// Qualifying Round
// D - Ominous Omino
//
// Adrian Dale
// 11/04/2015

#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

using namespace std;

int T; // No of test cases


void SolveFour(int R, int C)
{
	if (R == 1 || R == 2)
	{
		cout << "RICHARD";
		return;
	}

	if (R == 3)
	{
		if (C==3)
		{
			cout << "RICHARD";
			return;
		}
		else
		{
			cout << "GABRIEL";
			return;
		}
	}

	cout << "GABRIEL";
	return;
}

void SolveTestCase(int X, int R, int C)
{
	//cout << "Solving for  " << X << ", " << R  << ", " << C << endl;

	if (X == 1)
	{
		cout << "GABRIEL";
		return;
	}

	if (R > C)
	{
		int t = C;
		C = R;
		R = t;
	}

	if (X == 2)
	{
		if ((R*C) % 2 == 0)
		{
			cout << "GABRIEL";
			return;
		}
		else
		{
			cout << "RICHARD";
			return;
		}
	}

	if (X == 3)
	{
		if (R == 1)
		{
			cout << "RICHARD";
			return;
		}
		else if (R == 2)
		{
			if (C == 3)
			{
				cout << "GABRIEL";
				return;
			}
			else
			{
				cout << "RICHARD";
				return;
			}
		}
		else if (R == 3)
		{
				cout << "GABRIEL";
				return;
			
			
		}
		else if (R == 4)
		{
			cout << "RICHARD";
			return;
		}
	}
	else if (X == 4)
	{
		SolveFour(R, C);
	}
}


void ReadTestCases()
{
	string line;

	getline(cin, line);
	istringstream parser(line);
	parser >> T;

	int TestNo = 1;
	while (TestNo <= T)
	{
		getline(cin, line);
		parser.str(line);
		parser.clear();
		int X;
		int R;
		int C;
		parser >> X >> R >> C;

		cout << "Case #" << TestNo << ": ";
		SolveTestCase(X, R, C);
		cout << endl;

		++TestNo;
	}
}


int main()
{
	
	ReadTestCases();
	//SolveTestCase(4, 4, 4);
	
	return 0;
}
