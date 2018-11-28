// ConsoleApplication6.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int numIn;
	ifstream ifs("f.txt");
	ofstream ofs("a.txt");
	ifs >> numIn;

	for (int inNum = 0; inNum < numIn; inNum++) {
		string s;
		ifs >> s;
		string last;
		last.push_back(s[0]);
		for (int j = 1; j < s.length(); j++) {
			if (s[j] >= last[0])
				last = s.substr(j,1) + last;
			else
				last= last + s.substr(j, 1);
		}
		ofs << "Case #"<< inNum+1 << ": "<< last << endl;
	}


}
