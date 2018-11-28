#include <iostream> 
#include <fstream> 
#include <string>
#include <algorithm>
using namespace std;

// Problem D. Ominous Omino

int main(int argc, char* argv[])
{
	ifstream in("D-small.in");
	ofstream out("D-small.out");
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t)
	{
		int X, R, C;
		in >> X >> R >> C;
		bool fRichardWin = true;
		int area = R * C;
		if ( !(area % X) ) // possible for Richard to lose
		{
			if (X <= 2)
				fRichardWin = false;
			else if (X == 3)
				fRichardWin = min(R, C) < 2;
			else // X == 4
				fRichardWin = min(R, C) <= 2;
		}
		out << "Case #" << t << ": " << (fRichardWin ? "RICHARD" : "GABRIEL") << endl;
	}
	return 0;
}
