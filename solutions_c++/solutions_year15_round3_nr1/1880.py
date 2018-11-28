// Brattleship.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>

using namespace std;

ifstream f("A-small-attempt1.in");
ofstream g("output.txt");

int T, R, C, W;


int _tmain(int argc, _TCHAR* argv[])
{
	f >> T; 

	int x, nr;

	for (int i = 1; i <= T; i++)
	{
		f >> R; f >> C; f >> W;
		x = 0; nr = 0;

		while (nr + W <= C)
		{
			nr += W;
			x++;
		}
		if (C - nr)
		{
			x = x + W - 1 - C + nr;
			x = x + C - nr + 1;
		}
		else
			x = x + W - 1;
		x = x * R;

		g << "Case #" << i << ": " << x << endl;
	}

	f.close();
	g.close();
	return 0;
}

