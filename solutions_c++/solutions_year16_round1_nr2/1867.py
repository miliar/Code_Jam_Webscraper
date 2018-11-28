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
//	infile.open("src/B-small-attempt0.in");
	infile.open("src/B-large.in");

	// open a file in write mode.
	ofstream outfile;
	outfile.open("src/out");

	int T;
	infile>>T;
	for (int i = 1; i <= T; ++i)
	{
		int N;
		infile>>N;

		set<int>s;
		int M = 2*N*N - N;
		for(int j = 0; j < M; ++j)
		{
			int x;
			infile>>x;
			if(s.count(x))
				s.erase(x);
			else
				s.insert(x);
		}

		outfile<<"Case #"<<i<<": "<<*s.begin();
		for(set<int>::iterator it = ++s.begin(); it != s.end(); ++it)
			outfile<<" "<<*it;
		outfile<<endl;
	}
	outfile.close();
	return 0;
}
