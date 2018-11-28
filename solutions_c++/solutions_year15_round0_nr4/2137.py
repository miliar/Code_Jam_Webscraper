#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>
#include <list>

using namespace std;

int main()
{
	ifstream in("D-small-attempt3.in");
	ofstream out("D-small-attempt3.out");
	//ofstream out2("D-small-attempt2_.in");

	//ifstream in("D-large.in");
	//ofstream out("D-large.out");
	
	int iTasks;
	in >> iTasks;
	
	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		int X, R, C;
		in >> X >> R >> C;
		bool isRichardWins = false;
		if ((R * C) % X != 0)
		{
			isRichardWins = true;
		}
		else
		{
			//out2 << X << ' ' << R << " " << C << endl;
			for (int i = 0; i < (X + 1) / 2; i++)
			{
				int shortSide = i + 1;
				int longSide = X - i;
				if ((shortSide > min(R, C) && longSide > min(R, C)) ||
					shortSide > max(R, C) || longSide > max(R, C))
				{
					isRichardWins = true;
					break;
				}
				if (X > 3)
				{
					if ((shortSide >= min(R, C) && longSide >= min(R, C)))
					{
						isRichardWins = true;
						break;
					}
				}
			}
		}
		out << "Case #" << iCount << ": " << (isRichardWins ? "RICHARD" : "GABRIEL") << endl;

	}
	return 0;
}
