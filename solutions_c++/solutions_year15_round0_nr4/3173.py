#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	ifstream fin("test.in");
	ofstream fout("test.out");
	int CASES;
	fin >> CASES;
	for (int CASENUMBER = 1; CASENUMBER <= CASES; CASENUMBER++)
	{
		int X, R, C;
		fin >> X >> R >> C;

		bool gabewins = false;

		if (X == 1)
		{
			gabewins = true;
		}
		else if (X == 2)
		{
			if (R*C % 2 == 0)
			{
				gabewins = true;
			}
		}
		else if (X == 3)
		{
			if ((R == 2 && C == 3) || (R == 3 && C == 2) || (R == 3) && (C == 3) || (R == 3) && (C == 4) || (R == 4) && (C == 3))
			{
				gabewins = true;
			}
		}
		else
		{
			if ((R == 3 && C == 4) || (R == 4 && C == 3) || (R == 4 && C == 4))
			{
				gabewins = true;
			}
		}

		if (gabewins)
		{
			fout << "Case #" << CASENUMBER << ": " << "GABRIEL"<<endl;
		}
		else
		{
			fout << "Case #" << CASENUMBER << ": " << "RICHARD" << endl;
		}
	}
	return 0;
}