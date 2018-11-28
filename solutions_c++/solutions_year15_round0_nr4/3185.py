// Ominous_Omino.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

ifstream f("D-small-attempt2.in");
ofstream g("output.txt");

int T, X, R, C;

int _tmain(int argc, _TCHAR* argv[])
{
	int aux;
	f >> T;

	for (int i = 1; i <= T; i++)
	{
		f >> X;  f >> R;  f >> C;
		if ((R*C - X) % X != 0 || R*C - X < 0)
		{
			g << "Case #" << i << ": " << "RICHARD" << endl;
			continue;
		}
		aux = X / 2;
		if (aux > R || aux > C || X - aux > R || X - aux > C || ( X > R && X > C) || X > R + 1 || X > C + 1)
		{
			g << "Case #" << i << ": " << "RICHARD" << endl;
			continue;
		}
		g << "Case #" << i << ": " << "GABRIEL" << endl;
	}

	f.close();
	g.close();
	return 0;
}

