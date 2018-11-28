// Round1A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <math.h>

#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iomanip>

using namespace std;

const string OUTPUT_FILENAME = "output.txt";

template <typename T>
T StringToNumber ( const string &Text )
{
	istringstream ss(Text);
	T result;
	return ss >> result ? result : 0;
}

vector<string> &split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

struct InputLineData {
	string& lineBuf;
	vector<string>& splittedLineBuf;
	vector<int>& splittedLineNums;
};

struct InputDataSet {
	int lineNumber;
	vector<long double> line;
};

void Calc( InputDataSet& data , ofstream& ofs ) 
{
	long double ld;

	long double r = data.line[0];
	long double t = data.line[1];
	//long double x = sqrtl( t - r  * r );
	
	if( t > 1000 ) {
		return;
	}
	long double count = 0;
	long double a = r+1;
	long double sum = 0;
	while( sum <= t ) {
		sum += 2 * a - 1;
		a+=2;
		count++;
	}
	count--;
	//long double max_count = x - r;

	cout << "Case #" << data.lineNumber << ": " << count << endl;
	ofs <<  "Case #" << data.lineNumber << ": " << count << endl;
}

void MainFunc( ifstream& ifs ,  ofstream& ofs )
{
	string lineBuf;
	vector<string> splittedLineBuf;
	vector<long double> splittedLineNums;
	int lineCount = 0;
	int Tcount = 0;
	while(ifs) {
		splittedLineBuf.clear();
		lineBuf.clear();
		splittedLineNums.clear();

		if( !getline(ifs, lineBuf) ) {
			break;
		}
		split( lineBuf , ' ' , splittedLineBuf );
		
		for each( const string& out in splittedLineBuf ) {
			long long llInput = _atoi64(out.c_str());
			long double ld = llInput;
			splittedLineNums.push_back( ld );
			cout << setprecision(32) << ld << "/";
		}
		cout << endl;

		if( lineCount == 0 ) {
			Tcount = (int)splittedLineNums[0];
			lineCount++;
			continue;
		}
		else {
			InputDataSet data;
			data.lineNumber = lineCount;
			data.line = splittedLineNums;
			Calc( data , ofs );
			lineCount++;
		}

	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	if( argc > 3 || argc == 1 ) {
		cout << "invalid args" << endl;
		return -1;
	}

	ifstream ifs( argv[1] );
	ofstream ofs( OUTPUT_FILENAME );

	MainFunc( ifs , ofs );

	ifs.close();
	ofs.close();

	cout << "enter any key ..." << endl;
	char in;
	cin.get(in);

	return 0;
}

