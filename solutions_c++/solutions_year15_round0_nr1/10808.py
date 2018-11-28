#include "stdafx.h"
#include <stdlib.h>
#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <sstream>


using namespace std;




int main(int argc, const string argv[])
{
	ifstream myFile;
	ofstream output;
	output.open("StandingOvation_Output.txt");
	myFile.open(argv[0]);

	vector<int> integers;
	int testCase = 1;
	string line;

	//get the first line, which is a number representing the total number of test cases
	getline(myFile, line);
	char* charPntr = NULL;
	charPntr = &line[0];
	int numTestCases = atoi(charPntr);

	while (numTestCases > 0)
	{
		//get S_max
		getline(myFile, line);
		charPntr = &line[0];
		int Smax = atoi(charPntr);

		//Move to the beginning of the audience
		charPntr++;

		vector<int> audience;
		
		string numbers = charPntr;
		for (int i = 0; i < numbers.size(); i++)
		{
			if (numbers[i] != 32)
				audience.push_back((numbers[i] - '0'));
		}
		
		int count = audience[0];
		int needed = 0;

		for (int i = 1; i < audience.size(); i++)
		{
			if (audience[i] > 0)
			{
				if (i > count)
				{
					needed += (i - count);
					count += (audience[i] + needed);
				}
				else
				{
					count += audience[i];

				}
			}
		}


		output << "Case #" << testCase << ":" << " " << needed << "\n";
		
		testCase++;
		numTestCases--;
	}

	output.close();
	myFile.close();

	system("pause");
	return 0;
}