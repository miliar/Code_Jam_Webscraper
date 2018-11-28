#include <fstream>
using namespace std;

int Find(int * mass, int num, int current);

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	int i;

	int T;
	fin >> T;

	for (int t = 0; t < T; t++)
	{
		bool possible = false;
		int X, R, C;
		fin >> X >> R >> C;
		//fout << X << R << C << " " << R*C << endl;

		/*if (R * C % X != 0 || (X > R && X > C))
			possible = true;
		else
		{
			if (R * C < X * 2)
				possible = true;
			if (R * 2 < X || C * 2 < X)
				possible = true;
			
			int sz = (R * C - X * 2);
			if (sz % 2 != 0 || ((sz / 2) % X != 0))
			{
				if (R / 2 < X)
				{
					int figside = R / 2 + R % 2;
					int otherside = X - figside + 1;
					if (otherside != 1 && otherside * 2 >= C)
						possible = true;
				}
				
			}
		}*/
		if (X == 1)
		{
			possible = false;
		} 
		if (X == 2)
		{
			if (R == 1)
			{
				if (C == 1)
					possible = true;
				if (C == 2)
					possible = false;
				if (C == 3)
					possible = true;
				if (C == 4)
					possible = false;
			}
			if (R == 2)
			{
				possible = false;
			}
			if (R == 3)
			{
				if (C == 1)
					possible = true;
				if (C == 2)
					possible = false;
				if (C == 3)
					possible = true;
				if (C == 4)
					possible = false;
			}
		}
		if (X == 3)
		{
			if (R == 1)
			{
				possible = true;
			}
			if (R == 2)
			{
				if (C == 1)
					possible = true;
				if (C == 2)
					possible = true;
				if (C == 3)
					possible = false;
				if (C == 4)
					possible = true;
			}
			if (R == 3)
			{
				if (C == 1)
					possible = true;
				if (C == 2)
					possible = false;
				if (C == 3)
					possible = false;
				if (C == 4)
					possible = false;
			}
			if (R == 4)
			{
				if (C == 1)
					possible = true;
				if (C == 2)
					possible = true;
				if (C == 3)
					possible = false;
				if (C == 4)
					possible = true;
			}
		}
		if (X == 4)
		{
			if (R == 1)
			{
				possible = true;
			}
			if (R == 2)
			{
				if (C == 1)
					possible = true;
				if (C == 2)
					possible = true;
				if (C == 3)
					possible = true;
				if (C == 4)
					possible = true;
			}
			if (R == 3)
			{
				if (C == 1)
					possible = true;
				if (C == 2)
					possible = true;
				if (C == 3)
					possible = true;
				if (C == 4)
					possible = false;
			}
			if (R == 4)
			{
				if (C == 1)
					possible = true;
				if (C == 2)
					possible = true;
				if (C == 3)
					possible = false;
				if (C == 4)
					possible = false;
			}
		}

		//if (R * C % X != 0 || (X > R && X > C))
		//	possible = true;

		fout << "Case #" << (t + 1) << ": " << (possible ? "RICHARD" : "GABRIEL") << endl;
	}
}