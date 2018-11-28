#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>
#include <stdlib.h>

using namespace std;

vector<vector<string> > inputLines;
int noOfTestCases;
vector<string> result;

void input(char delim)
{
	string line;
	ifstream inputfile;

	inputfile.open("A-small-attempt3.in");

	while(getline(inputfile, line))
	{
		vector<string> inputWords;
		for(int length = line.length(), prev = 0, i = 0; i < length; i++)
		{
			if((i > 0 && line[i] != delim && line[i-1] == delim) || (i == 0 && line[i] != delim))
			{
				prev = i;
			}
			else if(i > 0 && line[i] == delim && line[i-1] != delim)
			{
				inputWords.push_back(line.substr(prev, i - prev));
			}
			if(i == length-1 && line[i] != delim)
			{
				inputWords.push_back(line.substr(prev, i - prev + 1));
			}
		}
		inputLines.push_back(inputWords);
	}

	//noOfTestCases = ;
}

void Evaluate()
{
	int firstChoice, secondChoice;
	int length = inputLines.size();

	noOfTestCases = atoi(inputLines[0][0].c_str());
	
	for(int i = 1; i < length; i = i+10)
	{
		firstChoice = atoi(inputLines[i][0].c_str());
		secondChoice = atoi(inputLines[i+5][0].c_str());
		int matched = 0;
		stringstream ss;

		for(int k = 0; k < 4; k++)
		{
			for(int m = 0; m < 4; m++)
			{
				if(inputLines[i+firstChoice][k] == inputLines[i+5+secondChoice][m])
				{
					ss << inputLines[i+firstChoice][k];
					matched++;
				}
			}
			if(matched > 1)
			{
				break;
			}
		}
		
		if(matched == 1)
		{
			result.push_back(ss.str());
		}
		else if(matched > 1)
		{
			result.push_back("Bad magician!");
		}
		else if(matched == 0)
		{
			result.push_back("Volunteer cheated!");
		}
	}
}

void output()
{
	ofstream outputfile;

	outputfile.open("output.txt", ios::app);

	for(int i = 1, j = 0; i <= noOfTestCases; i++, j++)
	{
		outputfile << "Case #" << i << ": " << result[j] << endl;
	}
}

int main()
{
	char delim = ' ';
	input(delim);
	Evaluate();
	output();

	return 0;
}

