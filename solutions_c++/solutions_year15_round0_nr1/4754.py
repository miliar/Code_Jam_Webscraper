//============================================================================
// Name        : Qualification.cpp
// Author      : GD Kalyan
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	string loc = "C:\\MyWorks\\Competitions\\CodeJam\\Data\\A-large";
	string inFile = loc + string(".in");
	string outFile = loc + string(".out");

	fstream myfile(inFile.c_str(), ios_base::in);
	fstream outfile(outFile.c_str(), ios_base::out);

	string line;

	if (!myfile.is_open() || !outfile.is_open())
	{
		cout << "Unable to open file";
		return 0;
	}

	int N = 0;
	int sMax = 1;
	myfile >> N;

	for(int i = 0; i<N; i++)
	{
		myfile >> sMax >> line;
		//cout << sMax << ", " << line << endl;

		short *shyHist = new short[sMax+1];
		for(int j=0; j<line.length(); j++)
			shyHist[j] = (short)(line[j] - '0');

		int minInv = 0;
		int nStand = shyHist[0];

		for(int shyL=1; shyL <= sMax; shyL++)
		{
			if( (nStand < shyL) && (shyHist[shyL]>0) )
			{
				minInv += (shyL - nStand);
				nStand += (shyL - nStand);
			}

			nStand += shyHist[shyL];
		}

		outfile << "Case #" << i+1 << ": " << minInv << endl;

		delete [] shyHist;
	}

	myfile.close();

	return 0;
}
