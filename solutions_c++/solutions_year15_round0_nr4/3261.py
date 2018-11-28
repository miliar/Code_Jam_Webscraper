// googlecj2015a.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <algorithm>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("j:\\D-small-attempt8.in");
	ofstream fout("j:\\output", ios_base::out | ios_base::trunc);
	string t;
	getline(fin, t);
	istringstream ss1(t, istringstream::in);
	int times = 0;
	ss1 >> times;
	for (int i = 0; i < times; ++i)
	{
		string line;
		getline(fin, line);
		istringstream stream1(line, istringstream::in);
		int X, R, C;
		stream1 >> X >> R >> C;

		int whowin = 0;
		
		if (X == 1)
			whowin = 1;
		else if (X == 2)
		{
			if ((R*C) % X == 0)
				whowin = 1;
		}
		else if (X == 3)
		{
			if (R*C == 6 || R*C==9 || R*C == 12)
				whowin = 1;
		}
		else if (X == 4)
		{
			if (R*C == 12 || R*C==16)
				whowin = 1;
		}

		fout << "Case #" << i + 1 << ": " << (whowin?"GABRIEL":"RICHARD")<< endl;
	}
	fout.close();
	system("pause");
	return 0;
}

