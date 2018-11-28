//============================================================================
// Name        : TicTacToeSimple.cpp
// Author      : Philipp Zigann
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

enum eState {gXwin, gOwin, ginprogress, gdraw};
//enum eValue {X = 1, Y = -1, T = 0 , Point = 10, empty = 11};

int res[7]; // 0-3 col// 4 row // 5,6 diag


int getValue(char symbol)
{
	switch (symbol)
	{
	case 'X': return 1;
	case 'O': return -1;
	case '.': return 10;
	case 'T': return 0;
	default:
		cout << "got default";
		exit (-1);
	}
}

eState handleTest()
{
	memset(res, 0, 7*sizeof(int));
	int value;
	string line;
	bool inprogress = false;

	for (int i = 0; i < 4; i++)
	{
		cin >> line;

		//if (line.empty())
		//	cin >> line;

		res[6] = 0;

		//cout << "line: " << line << " - ";
		for (int strpos = 0; strpos < 4; strpos++)
		{
			value = getValue(line[strpos]);
			//cout << value << ' ';
			res[strpos] += value;
			res[6] += value;
			if (i == strpos)
				res[4] += value;
			else if (i + strpos == 3)
				res[5] += value;
		}
		//cout << endl;

		if (res[6] > 4) inprogress = true;
		else if (res[6] < -2)
		{
			for (;i < 3; i++)
			{
				cin >> line;
				//cout << "drop line: " << line << endl;
			}
			return gOwin;
		}
		else if (res[6] > 2 )
		{
			for (;i < 3; i++)
			{
				cin >> line;
				//cout << "drop line: " << line << endl;
			}
			return gXwin;
		}
	}

	for (int resindex = 0; resindex < 6; resindex++)
	{
		if (res[resindex] > 4) inprogress = true;
		else if (res[resindex] < -2) return gOwin;
		else if (res[resindex] > 2 ) return gXwin;
	}

	if (inprogress)
		return ginprogress;
	else
		return gdraw;
}


int main() {
	eState currState;
	string line;
	//int values[4][4];


	unsigned int numTestCases = 0;
	cin >> line;

	numTestCases = strtol(line.c_str(), NULL, 10);

	for (unsigned int test = 1; test <= numTestCases; test++)
	{
		currState = handleTest();

		cout << "Case #" << test << ':';
		switch (currState)
		{
		case gXwin:
			cout << " X won" << endl;
			break;
		case gOwin:
			cout << " O won" << endl;
			break;
		case ginprogress:
			cout << " Game has not completed" << endl;
			break;
		case gdraw:
			cout << " Draw" << endl;
			break;
		default:
			cout << "error" << endl;
			return -1;
		}

	}

	return 0;
}
