#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

//file names
const string fileIn = "A-large.in";
const string fileOut = "A-large.out";

string intToString(int num);
int stringToInt(string text);

bool containsAll(string num);

int main()
{
	//ofstream save("settings.ini");
	ifstream load(fileIn);
	string line;

	getline(load, line);
	const int problemCount = stringToInt(line);
	vector<int> problems;

	for (int i = 0; i < problemCount; i++)
	{
		getline(load, line);
		problems.push_back(stringToInt(line));
	}

	load.close();

	//problems have been loaded
	//solve problems
	vector<string> solutions;

	string currentNum;
	string rawNum;
	int count;
	bool takeSolution;
	for (vector<int>::iterator problem = problems.begin(); problem != problems.end(); problem++)
	{
		currentNum = intToString(*problem);
		takeSolution = true;
		count = 0;
		while (!containsAll(currentNum))
		{
			if (currentNum == "0")
			{
				solutions.push_back("INSOMNIA");
				takeSolution = false;
				break;
			}

			count++;
			rawNum = intToString(*problem * count);
			currentNum += rawNum;
		}

		if (takeSolution)
		{
			solutions.push_back(rawNum);
		}
	}

	int j = 1;
	ofstream out(fileOut);
	for (vector<string>::const_iterator solution = solutions.begin(); solution != solutions.end(); solution++)
	{
		out << "Case #" << intToString(j) << ": ";
		out << *solution;
		out << "\n";
		j++;
	}
	out.close();

	return 1;
}

//int to string
string intToString(int num)
{
	stringstream ss;
	ss << num;
	return ss.str();
}

//string to int
int stringToInt(string text)
{
	int result;
	if (!(istringstream(text) >> result)) result = 0;
	return result;
}

bool containsAll(string num)
{
	string nums = "0123456789";
	bool round;
	for (string::iterator character = nums.begin(); character != nums.end(); character++)
	{
		round = false;
		for (string::iterator currentNum = num.begin(); currentNum != num.end(); currentNum++)
		{
			if (*character == *currentNum)
			{
				round = true;
				break;
			}
		}
		if (!round) return false;
	}
	return true;
}