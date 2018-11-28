
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

bool canFill(int X, int R, int C, bool enable_recursion = true)
{
	if (X == 1)
		return true;

	if ((R*C) % X != 0)
		return false;
	
	if (X == 2)
		return true;

	if (X == R*C)
		return false;

	if (R == 1 && X >= 3)
		return false;

	if (R == 2 && X >= 4)
		return false;

	if (R == 3 && X >= 6)
		return false;

	if (X >= 8)
		return false;

	// check mirror case
	if (enable_recursion && canFill(X, C, R, false) == false)
		return false;

	return true;
}

int main()
{
	FILE *in;
	if (fopen_s(&in, "D-small-attempt0.in", "r+") != 0)
		printf("The in file was not opened\n");

	fstream out("D-small-attempt0.out", ios::out);
	if (out.bad())
		printf("The out file was not opened\n");

	int T;
	fscanf_s(in, "%d", &T);

	for (int tc = 1; tc <= T; tc++)
	{
		int X, R, C;
		fscanf_s(in, "%d %d %d", &X, &R, &C);

		char* str;
		if (canFill( X, R, C ))
			str = "GABRIEL";
		else
			str = "RICHARD";

		cout << "Case #" << tc << ": " << str << endl;
		out << "Case #" << tc << ": " << str << endl;
	}

	_ASSERT(canFill(2, 2, 2) == true);
	_ASSERT(canFill(2, 1, 3) == false);
	_ASSERT(canFill(4, 4, 1) == false);
	_ASSERT(canFill(3, 2, 3) == true);
	_ASSERT(canFill(3, 2, 3) == true);
	cout << "Unit tests of canFill() are OK" << endl;

	out.close();
	getchar();
}