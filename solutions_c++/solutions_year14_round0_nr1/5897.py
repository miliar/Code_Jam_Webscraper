#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

#define SMALL

int main()
{
#ifdef SMALL
	ifstream in("a-small-attempt0.in");
	ofstream out("a-small.out");
#endif

	int testCases, cCase = 1;
	int r1, r2;
	int p1[4][4], p2[4][4];

	in >> testCases;

	while (cCase <= testCases)
	{
		in >> r1;

		for (int y = 0; y < 4; y++)
		{
			for (int x = 0; x < 4; x++)
			{
				in >> p1[x][y];
			}
		}

		in >> r2;

		for (int y = 0; y < 4; y++)
		{
			for (int x = 0; x < 4; x++)
			{
				in >> p2[x][y];
			}
		}

		int num1[4], num2[4];
		int c = 0, p;

		for (int x = 0; x < 4; x++)
		{
			num1[x] = p1[x][r1 - 1];
			num2[x] = p2[x][r2 - 1];
		}

		for (int x1 = 0; x1 < 4; x1++)
		{
			for (int x2 = 0; x2 < 4; x2++)
			{
				if (num2[x2] == num1[x1])
				{
					c++;
					p = num2[x2];
				}
			}
		}

		if (c == 0) out << "case #" << cCase << ": " << "Volunteer cheated!";
		else if (c > 1) out << "case #" << cCase << ": " << "Bad magician!";
		else if (c = 1) out << "case #" << cCase << ": " << p;

		out << endl;

		cCase++;
	}

	in.close();
	out.close();

	return 0;
}