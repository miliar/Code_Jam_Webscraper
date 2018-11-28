#include <iostream>
#include <string>
#include <fstream>
#include <vector>

#include <queue>

using namespace std;
using namespace stdext;

namespace
{
	bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile)
	{
		// input file
		readFile.open(inFile.c_str());
		if (!readFile)
		{
			cout << "Could not find '" << inFile << "'\n\n";
			return false;
		}

		// output file
		writeFile.open(outFile.c_str());
		if (!writeFile)
		{
			cout << "Could not find '" << outFile << "'\n\n";
			return false;
		}

		return true;
	}

	void print(ostream& os, int i, int card)
	{
		os << "Case #" << i+1 << ": ";
		if (card > 0)
			os << card << endl;
		else if (card < 0)
			os << "Bad magician!" << endl;
		else
			os << "Volunteer cheated!" << endl;
	}
}

int main()
{
	// files
	ifstream readFile;
	ofstream writeFile;
	
	//string fileIn("practice");
	string fileIn("A-small-attempt0.in");
	//string fileIn("large");

	if (!openFileHandles(readFile, fileIn, writeFile, fileIn + "_out.txt"))
		return -1;

	// read # of lines
	int numCases;
	readFile >> numCases;
	readFile.get();  // get rid of the newline

	// for each test case, ...
	for (int i = 0; i < numCases; ++i)
	{
		// read N
		int ans1;
		readFile >> ans1; --ans1;
		readFile.get();  // get rid of the newline

		vector<vector<int> > cards1(4, vector<int>(4));
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
				readFile >> cards1[j][k];
			readFile.get();  // get rid of the newline
		}

		// read N
		int ans2;
		readFile >> ans2; --ans2;
		readFile.get();  // get rid of the newline

		vector<vector<int> > cards2(4, vector<int>(4));
		for (int j = 0; j < 4; ++j)
		{
			for (int k = 0; k < 4; ++k)
				readFile >> cards2[j][k];
			readFile.get();  // get rid of the newline
		}

		// todo:
		int card = 0;
		for (int j = 0; j < 4; ++j)
		{
			if (card < 0)
				break; 

			for (int k = 0; k < 4; ++k)
			{
				if (card < 0)
					break;

				if (cards1[ans1][j] == cards2[ans2][k])
				{
					if (card == 0)
						card = cards1[ans1][j];
					else
					{
						card = -1;
						break;
					}
				}
			}
		}

		// case #s
		print(cout, i, card);
		print(writeFile, i, card);
	}  // for (n)

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}
