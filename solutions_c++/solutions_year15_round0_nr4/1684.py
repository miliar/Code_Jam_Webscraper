#include <vector>
#include <tuple>
#include <set>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main()
{
	ifstream fin;
	fin.open("D-small-attempt0.in");
	if (fin.is_open())
	{
		ofstream fout;
		fout.open("D-small-attempt0.out");
		int T;
		fin >> T;
		for (int i = 0; i < T; i++)
		{
			int X, R, C;
			string res = "RICHARD";
			fin >> X >> R >> C;
			if (X == 1) res = "GABRIEL"; else
				if (X < 7 && R*C%X == 0 && (X <= R || X <= C) && (X % 2 == 0 && (X / 2 <= R && X / 2 + 1 <= C || X / 2 <= C && X / 2 + 1 <= R) || X % 2 == 1 && (X + 1) / 2 <= R && (X + 1) / 2 <= C))
				{
					int M = min(R, C);
					if (X == 4 && M == 2 || X == 6 && M == 3) res = "RICHARD"; else res = "GABRIEL";
				}

			fout << "Case #" << i + 1 << ": " << res << endl;
		}
		fin.close();
		fout.close();
	}
	return 0;
}