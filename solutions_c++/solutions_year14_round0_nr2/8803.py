#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

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

	void print(ostream& os, int i, double y)
	{
		os << "Case #" << i+1 << ": " << std::fixed << std::setprecision(7) << y << endl;
	}
}

int main()
{
	// files
	ifstream readFile;
	ofstream writeFile;
	
	//string fileIn("practice");
	//string fileIn("small");
	string fileIn("large");

	if (!openFileHandles(readFile, fileIn + ".txt", writeFile, fileIn + "_out.txt"))
		return -1;

	// read # of lines
	int T;
	readFile >> T;
	readFile.get();  // get rid of the newline

	// for each test case, ...
	for (int t = 0; t < T; ++t)
	{
		double C, F, X;
		readFile >> C >> F >> X;
		readFile.get();  // get rid of the newline

		double y = 0;
		double curr = 0;
		double cps = 2;  // cookies per sec
		// todo:	

		double tc = X/cps,		// time with current cookie production
				tf = X/(cps+F),	// time with 1 extra farm
				tb = C/cps;      // time to buy a farm
		while (tc > (tf+tb))
		{
			y += tb,  // wait to buy a farm
			cps += F;  // rate increase

			tc = tf,
			tf = X/(cps+F),	// time with 1 extra farm
			tb = C/cps;      // time to buy a farm
		}
		// produce cookies with current cps
		y += X/cps;			

		//  "Case #x: y" -- x is case #, y is the height of bush number N - 1 
		//print(cout, t, y);
		print(writeFile, t, y);
	}  // for (n)

	// close file handles
	readFile.close();
	writeFile.close();

	// no error
	return 0;
}
