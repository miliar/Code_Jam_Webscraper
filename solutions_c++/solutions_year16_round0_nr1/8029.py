#pragma once

#include <iostream>
#include <fstream>
#include <set>
using namespace std;

class CountSheep
{
public:
	set<int> list{ 0,1,2,3,4,5,6,7,8,9 };

	void init()
	{
		list = set<int>{ 0,1,2,3,4,5,6,7,8,9 };
	}

	void main()
	{
		ifstream cin;
		cin.open("input.txt");
		ofstream out;
		out.open("output.txt");

		int caseNo;
		cin >> caseNo;

		for (int i = 0; i < caseNo; ++i)
		{
			init();

			unsigned long long n, realCopy;
			cin >> n;

			out << "Case #" << (i + 1) << ": ";
			if (n == 0)
			{
				out << "INSOMNIA" << endl;
				continue;
			}

			bool seen = false;

			for (int j = 1;; ++j)
			{
				auto copy = n * j;
				realCopy = copy;

				while (copy != 0)
				{
					int digit = copy % 10;
					copy /= 10;

					if (see(digit) == true)
					{
						seen = true;
						break;
					}
				}

				if (seen == true)
				{
					break;
				}
			}

			if (seen == true)
			{
				out << realCopy << endl;
			}
		}
	}

	bool see(int digit)
	{
		list.erase(digit);

		return list.empty();
	}
};