#include <fstream>
#include <string>
#include <sstream>
using namespace std;

string a[101];

string solve(string a[], int R, int C)
{
	ostringstream 	out;
	string  		DIRECTIONS = "<>^v";
	char 			original;
	int 			x, y, stepX, stepY;
	bool 			ok;
	int 			changes = 0;
	int 			cost;

	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if (a[i][j] == '.') continue;

			original 	= a[i][j];
			cost 		= 2;
			for (int k = 0; k < 4; k++)
			{
				a[i][j] = DIRECTIONS[k];

				switch (a[i][j])
				{
					case '<': stepX = -1; stepY =  0; break;
					case '>': stepX =  1; stepY =  0; break;
					case '^': stepX =  0; stepY = -1; break;
					case 'v': stepX =  0; stepY =  1; break;
				}

				x = j; y = i; ok = false;
				while ( (x >= 0) && (x < C) && (y >= 0) && (y < R) )
				{
					x += stepX;
					y += stepY;
					if ((x >= 0) && (x < C) && (y >= 0) && (y < R))
					{
						if (a[y][x] != '.')
						{
							ok = true;
							break;
						}
					}
				}

				if (ok)
				{
					if (a[i][j] == original)
					{
						cost = 0;
						break;
					}
					else
					{
						cost = 1;
					}
				}
			}
			if (cost == 2) return "IMPOSSIBLE";

			changes += cost;
		}
	}

	out << changes;

	return out.str();
}


int main()
{
	ifstream 	f("in.txt");
	ofstream 	g("out.txt");
	int 		T, R, C;

	f >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		f >> R >> C;
		for (int i = 0; i < R; i++)
			f >> a[i];
		g << "Case #" << testCase << ": " << solve(a, R, C) << endl;
	}

	return 0;
}
