//============================================================================
// Name        : Problem.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	// open a file in read mode.
	ifstream infile;
//	infile.open("src/in");
//	infile.open("src/A-small-attempt0.in");
	infile.open("src/A-large.in");

	// open a file in write mode.
	ofstream outfile;
	outfile.open("src/out");

	int T;
	infile>>T;
	for (int i = 1; i <= T; ++i)
	{
		string in, s = "";
		infile>>in;
		s+=in[0];
		for (size_t j = 1; j < in.size(); ++j)
			if(in[j]>=s[0])
				s = in[j]+s;
			else
				s = s+ in[j];

		outfile<<"Case #"<<i<<": "<<s<<endl;
	}
	outfile.close();
	return 0;
}
