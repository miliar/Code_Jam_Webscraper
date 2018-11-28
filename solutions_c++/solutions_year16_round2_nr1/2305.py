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
//	infile.open("src/A-small-attempt1.in");
	infile.open("src/A-large.in");

	// open a file in write mode.
	ofstream outfile;
	outfile.open("src/out");

	int T;
	infile>>T;
	for (int i = 1; i <= T; ++i)
	{
		vector<int> data(30,0);
		string str;
		infile>>str;
		for(size_t j = 0; j < str.size(); ++j)++data[str[j]-'A'];

		vector<int> num(10,0);

		num[0] = data['Z'-'A'];
		num[2] = data['W'-'A'];
		num[4] = data['U' - 'A'];
		num[6] = data['X'-'A'];
		num[7] = data['S' - 'A'] - num[6];
		num[5] = data['V' - 'A'] - num[7];
		num[1] = data['O' - 'A'] - num[0]-num[2]-num[4];
		num[3] = data['R'-'A'] - num[0]-num[4];
		num[8] = data['H'-'A'] - num[3];
		num[9] = (data['N'-'A']-num[1]-num[7])/2;

		string s;
		for (int j = 0; j < 10;++j)
			s += string(num[j], '0'+j);
		outfile<<"Case #"<<i<<": "<<s<<endl;
	}
	outfile.close();
	return 0;
}
