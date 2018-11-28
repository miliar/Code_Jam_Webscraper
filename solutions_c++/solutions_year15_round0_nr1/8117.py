// Lab.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <cassert>
#include <functional>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	unsigned t = 0;
	ifstream in("in.txt");
	in >> t;
	ofstream out("out.txt");
	for (unsigned i = 0; i < t; ++i) {
		unsigned sm;
		string s;
		in >> sm;
		in >> s;
		unsigned people = 0;
		unsigned result = 0;
		for (unsigned j = 0; j < sm + 1; ++j) {
			if (people < j) {
				result += j - people;
				people = j;
			}
			people += (s[j] - '0');
		}
		out << "Case #" << (i + 1) << ": " << result << endl;
	}
	return 0;
}

	