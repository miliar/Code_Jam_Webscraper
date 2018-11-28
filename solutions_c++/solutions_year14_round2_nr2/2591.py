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

	void print(ostream& os, int i, int count)
	{
		os << "Case #" << i+1 << ": " << count << endl;
	}
}

int main()
{
	// files
	ifstream readFile;
	ofstream writeFile;

	//string fileIn("practice.txt");
	string fileIn("small.in");
	//string fileIn("large.txt");

	if (!openFileHandles(readFile, fileIn, writeFile, fileIn + "_out.txt"))
		return -1;

	// read # of lines
	int T;
	readFile >> T;
	readFile.get();  // get rid of the newline

	// for each test case, ...
	for (int t = 0; t < T; ++t)
	{
		// read N
		int A, B, K;
		readFile >> A >> B >> K;
		readFile.get();  // get rid of the newline

		// todo:	
		int count = 0;
		for (int a = 0; a < A; ++a)
			for (int b = 0; b < B; ++b)
				if ((a&b) < K)
					++count;

		//  "Case #x: y" -- x is case #, y is the height of bush number N - 1 
		//print(cout, t, count);
		print(writeFile, t, count);
	}  // for (n)

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}

