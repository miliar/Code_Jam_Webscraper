#pragma once

#include <fstream>
#include <string>
using namespace std;

class Pancake
{
public:
	void main()
	{
		ifstream cin("input.txt");
		ofstream output("output.txt");

		int caseNo;
		cin >> caseNo;

		for (int i = 0; i < caseNo; ++i)
		{
			string line;
			cin >> line;

			int revertCount = 0;

			for (int j = 0; j < line.size() - 1; ++j)
			{
				char c = line[j];

				int endIndex = -1;

				while (true)
				{
					++j;
					if (line[j] != c)
					{
						endIndex = --j;
						break;
					}
				}

				if (endIndex == line.size() - 1 && line[endIndex] == '+')
				{
					break;
				}

				revert(line, c, 0, endIndex);
				++revertCount;
			}

			if (line[0] == '-')
			{
				++revertCount;
			}

			output << "Case #" << (i + 1) << ": " << revertCount << endl;
		}
	}

	void revert(string& line, char c, int s, int e)
	{
		if (c == '-')
		{
			c = '+';
		}
		else
		{
			c = '-';
		}

		for (int i = s; i <= e; ++i)
		{
			line[i] = c;
		}
	}
};