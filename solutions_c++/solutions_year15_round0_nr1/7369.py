#include <iostream>
#include <string>
#include <string.h>
#include <fstream>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("A-large.in");
	out.open("output.txt");

	int cases = 0;
	int sMax = 0;
	string sLevel = "";

	in >> cases;

	for (int index = 0; index < cases; index++)
	{
		int totalStanding = 0;
		int numNeeded = 0;
		
		in >> sMax;
		in >> sLevel;

		int length = sLevel.size();
		for (int i = 0; i < length; i++)
		{
			char tempChar = sLevel.at(i);
			int numAtIndex = 0;

			switch(tempChar)
			{
			case '0':
				numAtIndex = 0;
				break;
			case '1':
				numAtIndex = 1;
				break;
			case '2':
				numAtIndex = 2;
				break;
			case '3':
				numAtIndex = 3;
				break;
			case '4':
				numAtIndex = 4;
				break;
			case '5':
				numAtIndex = 5;
				break;
			case '6':
				numAtIndex = 6;
				break;
			case '7':
				numAtIndex = 7;
				break;
			case '8':
				numAtIndex = 8;
				break;
			case '9':
				numAtIndex = 9;
				break;
			}

				while (totalStanding < i)
				{
					numNeeded++;
					totalStanding++;
				}

			totalStanding += numAtIndex;
		}

		out << "Case #" << index + 1 << ": " << numNeeded << endl;
	}

	out.close();
	in.close();
	return 0;
}