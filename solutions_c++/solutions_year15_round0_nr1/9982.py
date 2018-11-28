#include <iostream>
#include<fstream>
#include <string>

using namespace std;


int main()
{
	int testCases = 0;
	int input[100][8];
	string line[256];
	
	std::ifstream file("A-small-attempt1.in");
	std::string str;
	for (int i = 0; file.good(); i++)
	{
		getline(file, line[i]);
		str = line[i];
		if (i == 0)
		{
			testCases = std::stoi(str);
		}
		else
		{
			int iCharNumber = 1;
			int iCharCnt = 0;
			for (char & c : str)
			{
				if (iCharNumber == 2)
				{
					iCharNumber++;
					continue;
				}
				input[i - 1][iCharCnt] = c - 48;
				iCharCnt++;
				iCharNumber++;
			}
		}
	}

	ofstream myfile("output.txt");
	if (myfile.is_open())
	{

		for (int iCntTestCase = 0; iCntTestCase < testCases; iCntTestCase++)
		{
			int audStan = 0;
			int i = 1;
			int iNumberOfInviteRequired = 0;
			do
			{
				audStan = audStan + input[iCntTestCase][i];
				if (audStan < i)
				{
					audStan++;
					iNumberOfInviteRequired++;
				}
				i++;
			} while (audStan < input[iCntTestCase][0]);

			myfile << "Case #" << (iCntTestCase + 1) << ": " << iNumberOfInviteRequired << endl;
		}
	}
	myfile.close();
	return 0;
}
