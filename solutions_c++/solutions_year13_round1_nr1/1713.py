#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <stack>

#define PI 3.14159265359

using namespace std;
using namespace stdext;

bool openFileHandles(ifstream& readFile, const string& inFile, ofstream& writeFile, const string& outFile);

namespace
{
	typedef long long ll;

	const ll MAX = ll(1e18);
}

int main()
{
	// files
	ifstream readFile;
	ofstream writeFile;
	
	string fileIn = //"practice";
		            "small";
	                //"large";

	if (!openFileHandles(readFile, fileIn + ".in", writeFile, fileIn + ".out"))
		return -1;

	// read # of lines
	int T;
	readFile >> T;
	readFile.get();  // get rid of the newline

	// for each test case, ... 
	for (int i = 1; i <= T; ++i)
	{
		// 1. read in file
		ll r, t;
		readFile >> r >> t;

		int count = 0;
		while (true)
		{
			double currPaint = (2*r + 1);
			t -= currPaint;

			if (t < 0)
				break;

			++count;
			r += 2;
		}


		//cout << "Case #" << i << ": " << count << endl;
		writeFile << "Case #" << i << ": " << count << endl;

	}  // for (t)

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}

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
