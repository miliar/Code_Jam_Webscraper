
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <ctime>

//#define LARGE_IP
using namespace std;

int main()
{

	auto t = std::time(nullptr);
	auto tm = *std::localtime(&t);
	std::cout << std::put_time(&tm, "Start time : %M:%S") << std::endl;

	ofstream lOutputFile;
#ifdef LARGE_IP
	ifstream lInputFile("D-large-practice.in");
	lOutputFile.open("D-large-practice.out");
#else
	ifstream lInputFile("D-small-practice.in");
	lOutputFile.open("D-small-practice.out");
#endif

	int T = 0;

	lInputFile >> T;
	
	for (int t = 1; t <= T; t++)
	{
		int X = 0, R = 0, C = 0;
		bool lbGWin = true;
		lInputFile >> X >> R >> C;

		if ((X >= 7) || ((R < X) && (C < X)) || ((R*C)%X != 0))
		{
			lbGWin = false;
		}
		else
		{
			switch (X)
			{
			case 1:
			case 2:
				lbGWin = true;
				break;
			case 3:
				if (R<2 || C<2)
					lbGWin = false;
				break;
			case 4:
				if (R<3 || C<3)
					lbGWin = false;
			default:
				break;
			}
		}

		if (lbGWin)
		{
			lOutputFile << "Case #" << t << ": GABRIEL"<< endl;
		}
		else
		{
			lOutputFile << "Case #" << t << ": RICHARD" << endl;
		}
	}

	lInputFile.close();
	lOutputFile.close();

	t = std::time(nullptr);
	tm = *std::localtime(&t);
	std::cout << std::put_time(&tm, "End Time : %M:%S") << std::endl;
	return 0;
}
