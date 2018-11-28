// gcjqa.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>

using namespace std;

/*std::string line;
while (std::getline(infile, line))
{
    std::istringstream iss(line);
    int a, b;
    if (!(iss >> a >> b)) { break; } // error

    // process pair (a,b)
}*/

int r(const string&);

int n(const string& s){
	if (s=="")
		return 0;
	if (s.back()=='-'){
		return n(s.substr(0, s.size()-1));
	}
	if (s.back()=='+'){
		return 1+r(s.substr(0, s.size()-1));
	}
}

int r(const string& s){
	if (s=="")
		return 0;
	if (s.back()=='+'){
		return r(s.substr(0, s.size()-1));
	}
	if (s.back()=='-'){
		return 1+n(s.substr(0, s.size()-1));
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream a("D:\\gcj\\B-large.in");
	ofstream o("D:\\gcj\\output.txt");
	int nr; a>>nr;
	std::string line;
	std::getline(a, line);
	for (int i=0; i<nr; i++){
		std::string line;
		std::getline(a, line);
		o << "Case #" << (i+1) << ": " << r(line) << endl;
//		cerr << "Case #" << (i+1) << ": " << r(line) << endl;
//		cerr << line << endl;

	}
	a.close();
	o.close();
//	char c; cin >> c;
	return 0;
}

