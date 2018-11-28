// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream in("A-large.in");
	std::ofstream out("A-large.out");

	vector <char> list;

	int T, Smax, minNum, total, add;
	char temp;

	in >> T;

	for (int i = 0; i < T; i++)
	{
		in >> Smax;
		list.clear();
		for (int j = 0; j < Smax + 1; j++)
		{
			in >> temp;
			list.push_back(temp);
		}

		minNum = total = 0;
		for (int j = 0; j < list.size() - 1; j++)
		{
			total += list.at(j) - '0';
			if ((list.at(j + 1) - '0') > 0)
			{
				if (total < (j + 1))
				{
					add = (j + 1) - total;
					total += add;
					minNum += add;
				}
			}
		}

		out << "Case #" << i + 1 << ": " << minNum << endl;
	}

	return 0;
}

