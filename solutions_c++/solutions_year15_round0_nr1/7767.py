#include <iostream>
#include <fstream>
#include "../../ZKR4X/lib/zfile.h"

using namespace std;;

int main(int argc, char **argv)
{
	std::string path = argv[0];
	ZFile fileIn("./in.txt", ios::in);

	if(!fileIn)
		return 1;

	ZFile fileOut("./out.txt", ios::out);

	if(!fileOut)
		return 2;


	int T = 0;
	fileIn >> T;

	for (int i = 1; i <= T; i++)
	{
		int smax;
		fileIn >> smax;
		string s;
		fileIn >> s;
		
		int neededPpl = 0, totalPpl = 0;

		for (int j = 0;j <= smax; j++)
		{
			if(totalPpl < j)
			{
				neededPpl += j - totalPpl;
				totalPpl += j - totalPpl;
			}
			totalPpl += int(s[j]) - 48;
		}
		
		fileOut << "Case #" << i << ": " << neededPpl << "\n";
	}

	return 0;
}
