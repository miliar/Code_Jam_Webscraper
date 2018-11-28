#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

#if 0
istream& in = cin;
ostream& out = cout;
#else
istream& in = ifstream("in");
ostream& out = ofstream("out");
#endif

bool solve(int X, int R, int C)
{
	if (R > C)
		swap(R, C);

	if (R*C % X > 0)
		return false;

	if (X == 1)
		return true;

	if (X == 2)
		return R*C % X == 0;

	if (X == 3)
	{
		if (R == 1) return false;
		if (R == 2)
		{
			if (C == 2) return false;
			else return true;
		}
		if (R == 3) return true;
	}

	if (X == 4)
	{
		if (R == 1) return false;
		if (R == 2) return false;
		if (R == 3)
		{
			if (C == 3) return false;
			else return true;
		}
		if (R == 4)
			return true;
	}

	_asm int 3;
}

int main()
{
	int T, X, R, C;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		in >> X >> R >> C;
		bool b = solve(X, R, C);

		string name = b ? "GABRIEL" : "RICHARD";
		out << "Case #" << t << ": " << name << endl;
	}

	return 0;
}