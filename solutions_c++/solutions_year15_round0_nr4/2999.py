#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

string Solve (int X, int R, int C)
{
	if ((R * C) % X != 0)
		return "RICHARD";
	if (C == 1 && X > 2)
		return "RICHARD";
	if (C == 2 && R == 4 && X == 4)
		return "RICHARD";
	if (C == 2 && R == 2 && X == 4)
		return "RICHARD";
	return "GABRIEL"; // he can completely fill the shit
}

int main()
{
	ofstream fout("output.txt");
	ifstream fin("input.txt");
	int T;
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		int R, C, X;
		fin >> X >> R >> C;
		if (R < C)
			swap(R, C);
		fout << "Case #" << i + 1 << ": " << Solve(X, R, C) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}