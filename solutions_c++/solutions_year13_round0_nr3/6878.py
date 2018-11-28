#include "Number.h"

#include <fstream>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
	if(argc != 2)
	{
		//cout << "Insufficient Input arguments" << endl << "Usage ::" << endl;
		//cout << argv[0] << " <Test Cases File Path>" << endl;
		return -1;
	}

	//cout << "Opening Input file :: " << argv[1] << endl;
	ifstream inputFile(argv[1]);
	string strLine;
	int index = 0, noOFTestCases;
	long long upperLimit, lowerLimit;
	long curTotalNoOfSAF = 0;
	
	if(inputFile.is_open())
	{
		while(inputFile.good())
		{
			getline(inputFile, strLine);
			//cout << "Current Line :: " << strLine << ", CurrentIndex :: " << index << endl;
			if(index == 0)
			{
				noOFTestCases = atoi(strLine.c_str());
			}
			else if(index <= noOFTestCases)
			{
				curTotalNoOfSAF = 0;
				size_t pos = strLine.find_first_of(" ");
				string lowerLim = strLine.substr(0, pos);
				string upperLim = strLine.substr(pos + 1, strLine.length());
				upperLimit = atoi(upperLim.c_str());
				lowerLimit = atoi(lowerLim.c_str());

				for(long long curIndex = lowerLimit; curIndex <= upperLimit; curIndex++)
				{
					Number curNum(curIndex);
					if(curNum.isFairAndSquare())
					{
						curTotalNoOfSAF++;
						//cout << "Current Fair And Simple No " << curNum << endl;
					}
				}

				cout << "Case #" << index << ": " << curTotalNoOfSAF << endl;
			}
			else
			{
				//cout << "Input test cases [" << index << "] exceeded Given Number of test cases [" << noOFTestCases << "]" << endl;
				return -1;
			}	
			
			index++;
		}

		inputFile.close();
	}
	else
	{
		//cout << "Failed to open Input file " << argv[1] << " to read test cases." << endl;
		return -1;
	}

	return 0;
}