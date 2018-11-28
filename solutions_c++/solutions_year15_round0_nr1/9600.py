// CodeJam1.cpp : Defines the entry point for the console application.
//
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int getNeeded (const string &ShyArr)
{
	int sum (0), needed (0);
	int stringlength = ShyArr.length();
	for (int i=0; i < stringlength ; i++)
	{
		if ((sum < i) && (ShyArr[i] != '0'))
		{
			needed += i - sum;
			sum += i - sum;
		}

		sum += (ShyArr[i] - '0');
	}

	return needed;
}

void processTestCases(string &inputShyness, int testIndex, ofstream &outfile)
{
	outfile << "Case #" << testIndex << ": " << getNeeded(inputShyness) << endl;

}

void run (const string &FileName)
{

	ifstream f(FileName.c_str());
	if (!f)
	{
		cerr << "Error: Could not open file " << FileName;
		return;
	}
	
	ofstream outfile("OutputCJ1.txt");
	if (!outfile)
	{
		cerr << "Error: Could not open file " << "OutputCJ1.txt";
		return;
	}

	string line;
	f >> line;
	
	stringstream sstr (line);
	int numTestCases = 0;
	sstr >> numTestCases;
	string maxShyness, inputShyness;

	for (int ii=0; ii < numTestCases; ii++)
	{
		f >> maxShyness;
		f >> inputShyness;
		processTestCases(inputShyness,ii+1, outfile);


	}

}

int main(int argc, char * argv[])
{
	run("A-large.in");
	
	return 0;
}

