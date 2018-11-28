//============================================================================
// Name        : google_2013_cj_fair_and_square.cpp
// Author      : blue
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool is_palindrom(unsigned long i)
{
	if (i < 10)
	{
		return true;
	}
	else if (i < 100)
	{
		if (i % 10 == i / 10)
		{
			return true;
		}
	}
	else if (i < 1000)
	{
		if (i % 10 == i / 100)
		{
			return true;
		}
	}

	return false;
}

int main()
{
	cout << "google_2013_cj_fair_and_square" << endl;

	int num;
	ifstream in;
	ofstream out;

	in.open("in.txt", ifstream::in);
	if (!in.good())
	{
		cout << "In file bad" << endl;
		return -1;
	}

	out.open("out.txt", ofstream::out);
	if (!out.good())
	{
		cout << "Out file bad" << endl;
		return -1;
	}

	in >> num;

	for (int i = 0; i < num; i++)
	{
		unsigned long min = 0;
		unsigned long max = 0;
		unsigned long sq = 0;
		unsigned long result = 0;
		unsigned int palindromes = 0;

		in >> min;
		in >> max;

		cout << "\nCase #" << i + 1 << " of " << num << " Min:" << min
				<< " Max:" << max << endl;

		sq = static_cast<typeof(sq)>(sqrt(max));

		cout << "Smallest square is " << sq << endl;

		do
		{
			cout << " test " << sq << endl;
			;
			if (is_palindrom(sq))
			{
				cout << "  is a palindrom " << sq << endl;
				;
				result = sq * sq;

				if (result < min)
				{
					break;
				}
				else if (is_palindrom(result))
				{
					cout << "   FOUND palindrome! " << result << endl;
					palindromes++;
				}
			}
			sq--;
		} while (sq > 0);

		out << "Case #" << i + 1 << ": " << palindromes << endl;
	}

	in.close();
	out.close();
	return 0;
}
