#include<iostream>
#include<fstream>
#include<string>
using namespace std;

string WhoWInsX2(int R, int C)
{
	if (R == 1 && C == 1)
		return "RICHARD";
	if (R == 1 && C == 2)
		return "GABRIEL";
	if (R == 1 && C == 3)
		return "RICHARD";
	if (R == 1 && C == 4)
		return "GABRIEL";
	if (R == 2 && C == 1)
		return "GABRIEL";
	if (R == 2 && C == 2)
		return "GABRIEL";
	if (R == 2 && C == 3)
		return "GABRIEL";
	if (R == 2 && C == 4)
		return "GABRIEL";
	if (R == 3 && C == 1)
		return "RICHARD";
	if (R == 3 && C == 2)
		return "GABRIEL";
	if (R == 3 && C == 3)
		return "RICHARD";
	if (R == 3 && C == 4)
		return "GABRIEL";
	if (R == 4 && C == 1)
		return "GABRIEL";
	if (R == 4 && C == 2)
		return "GABRIEL";
	if (R == 4 && C == 3)
		return "GABRIEL";
	if (R == 4 && C == 4)
		return "GABRIEL";
}

string WhoWInsX3(int R, int C)
{
	if (R == 1 && C == 1)
		return "RICHARD";
	if (R == 1 && C == 2)
		return "RICHARD";
	if (R == 1 && C == 3)
		return "RICHARD";
	if (R == 1 && C == 4)
		return "RICHARD";
	if (R == 2 && C == 1)
		return "RICHARD";
	if (R == 2 && C == 2)
		return "RICHARD";
	if (R == 2 && C == 3)
		return "GABRIEL";
	if (R == 2 && C == 4)
		return "RICHARD";
	if (R == 3 && C == 1)
		return "RICHARD";
	if (R == 3 && C == 2)
		return "GABRIEL";
	if (R == 3 && C == 3)
		return "GABRIEL";
	if (R == 3 && C == 4)
		return "GABRIEL";
	if (R == 4 && C == 1)
		return "RICHARD";
	if (R == 4 && C == 2)
		return "RICHARD";
	if (R == 4 && C == 3)
		return "GABRIEL";
	if (R == 4 && C == 4)
		return "RICHARD";
}

string WhoWInsX4(int R, int C)
{
	if (R == 1 && C == 1)
		return "RICHARD";
	if (R == 1 && C == 2)
		return "RICHARD";
	if (R == 1 && C == 3)
		return "RICHARD";
	if (R == 1 && C == 4)
		return "RICHARD";
	if (R == 2 && C == 1)
		return "RICHARD";
	if (R == 2 && C == 2)
		return "RICHARD";
	if (R == 2 && C == 3)
		return "RICHARD";
	if (R == 2 && C == 4)
		return "RICHARD";
	if (R == 3 && C == 1)
		return "RICHARD";
	if (R == 3 && C == 2)
		return "RICHARD";
	if (R == 3 && C == 3)
		return "RICHARD";
	if (R == 3 && C == 4)
		return "GABRIEL";
	if (R == 4 && C == 1)
		return "RICHARD";
	if (R == 4 && C == 2)
		return "RICHARD";
	if (R == 4 && C == 3)
		return "GABRIEL";
	if (R == 4 && C == 4)
		return "GABRIEL";
}

string WhoWins(int X, int R, int C)
{
	switch (X)
	{
		case 1:
			return "GABRIEL";
		case 2:
			return WhoWInsX2(R, C);
		case 3:
			return WhoWInsX3(R, C);
		case 4:
			return WhoWInsX4(R, C);
	}
}

int main()
{
	ifstream fin("D-small-attempt4.in");
	ofstream fout("output.txt");

	int T, i, j, X, R, C;
	fin >> T;
	for (i = 0; i < T; i++)
	{
		fin >> X;
		fin >> R;
		fin >> C;

		fout << "Case #" << i + 1 << ": " << WhoWins(X,R,C) << endl;
	}
	return 0;
}