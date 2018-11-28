#include <fstream>

using namespace std;

ifstream fin ("D.in");
ofstream fout ("D.out");

main ()
{
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++)
	{
		int X, R, C;
		fin >> X >> R >> C;
		if (X >= 7)
		{
			fout << "Case #" << t << ": RICHARD" << endl;
			continue;
		}
		if ((R * C) % X != 0)
		{
			fout << "Case #" << t << ": RICHARD" << endl;
			continue;
		}
		if (R < X && C < X)
		{
			fout << "Case #" << t << ": RICHARD" << endl;
			continue;
		}
		if (R >= X && C >= X)
		{
			fout << "Case #" << t << ": GABRIEL" << endl;
			continue;
		}
		if (R > C)
		{
			int tmp = R;
			R = C;
			C = tmp;
		}
		switch (X)
		{
			case 1: case 2:
				fout << "Case #" << t << ": GABRIEL" << endl;
				break;
			case 3:
				if (R == 1) fout << "Case #" << t << ": RICHARD" << endl;
				else fout << "Case #" << t << ": GABRIEL" << endl;
				break;
			case 4:
				if (R == 1)
				{
					fout << "Case #" << t << ": RICHARD" << endl;
					break;
				}
				if (R == 2)
				{
					if (C < 6) fout << "Case #" << t << ": RICHARD" << endl;
					else fout << "Case #" << t << ": GABRIEL" << endl;
					break;
				}
				fout << "Case #" << t << ": GABRIEL" << endl;
				break;
			case 5:
				if (R == 1 || R == 2)
				{
					fout << "Case #" << t << ": RICHARD" << endl;
					break;
				}
				fout << "Case #" << t << ": GABRIEL" << endl;
				break;
			case 6:
				if (R == 1 || R == 2 || R == 3)
				{
					fout << "Case #" << t << ": RICHARD" << endl;
					break;
				}
				fout << "Case #" << t << ": GABRIEL" << endl;
				break;				
		}
	}
}
