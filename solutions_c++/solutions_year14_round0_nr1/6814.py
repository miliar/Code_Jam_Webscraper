// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	int rowId1, rowId2;
	string buf;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		ostringstream convert;
		cin >> rowId1;

		vector<int> row1(4);
		int j = 1;
		while (j++ < rowId1)
		{
			cin >> buf;
			cin >> buf;
			cin >> buf;
			cin >> buf;
		}

		for (int k = 0; k < 4; k++)
		{
			cin >> row1[k];
		}

		while (j++ <= 4)
		{
			cin >> buf;
			cin >> buf;
			cin >> buf;
			cin >> buf;
		}
		
		j = 1;
		cin >> rowId2;
		vector<int> row2(4);
		while (j++ < rowId2)
		{
			cin >> buf;
			cin >> buf;
			cin >> buf;
			cin >> buf;
		}

		for (int k = 0; k < 4; k++)
		{
			cin >> row2[k];
		}
		while (j++ <= 4)
		{
			cin >> buf;
			cin >> buf;
			cin >> buf;
			cin >> buf;
		}

		string res;
		for (auto m : row1)
		{
			auto find = std::find(row2.begin(), row2.end(), m);
			if (find != row2.end())
			{
				if (res.empty())
				{
					convert << m;
					res = convert.str();
				}
				else
				{
					res = "Bad magician!";
					break;
				}
			}
		}
		if (res.empty())
			res = "Volunteer cheated!";

		cout << "Case #" << i + 1 << ": " << res << endl;
	}

	return 0;
}

