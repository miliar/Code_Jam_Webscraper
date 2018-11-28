#include <iostream>
#include <ios>
#include <fstream>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <set>
#include <bitset>

using namespace std;

string flip(string &str)
{
	for (size_t i = 0; i < str.length(); ++i)
	{
		if (str[i] == '+')
		{
			str[i] = '-';
		}
		else
		{
			str[i] = '+';
		}
	}
	return str;
}

int countFlip(string line)
{
	if (line.length() == 1)
	{
		if (line == "+")
			return 0;
		else
			return 1;
	}

	int rightMost = line.length() - 1;
	if (line[rightMost] == '+')
	{
		return countFlip(line.substr(0, rightMost));
	}
	else
	{
		return countFlip(flip(line.substr(0, rightMost))) + 1;
	}
	
	return 0;
}

int main(int argc, char *argv[])
{
	if (argc < 2) {
		cout << "Missing arguments!" << endl;
		return -1;
	}

	ifstream inputFile(argv[1]);
	string outputFileName = string(argv[1]) + ".out";
	ofstream outputFile(outputFileName.c_str(), ios::out | ios::trunc);
	if (!inputFile || !outputFile) {
		cout << "Open file error" << endl;
		return -2;
	}

	string line;
	getline(inputFile, line);
	int caseNum = atoi(line.c_str());
	int i = 0;
	while (i < caseNum) {
		getline(inputFile, line);
		outputFile << "Case #" << ++i << ": " << countFlip(line) << endl;
	}
	outputFile.flush();
	inputFile.close();
	outputFile.close();
	return 0;
}
