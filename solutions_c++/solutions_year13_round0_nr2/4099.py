//============================================================================
// Name        : Lawnmower.cpp
// Author      : Jitesh
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <istream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#include <boost/numeric/ublas/matrix.hpp>

#include <iomanip>
#include <math.h>
#include <stdio.h>
#include <string.h>

using namespace std;

class lawnDS {
public:
	map<int, vector<pair<int, int> > > heights;
	void insert(int value, int x, int y)
	{
		vector<pair<int, int> >& itr = heights[value];
		itr.push_back(make_pair(x, y));
	}

	void print()
	{
		for(map<int, vector<pair<int, int> > >::reverse_iterator itr = heights.rbegin(); itr != heights.rend(); ++itr) {
			cerr << "[" << itr->first << "]";
			for(vector<pair<int, int> >::iterator itr2 = itr->second.begin(); itr2 != itr->second.end(); ++itr2) {
				cerr << "(" << itr2->first << ", " << itr2->second << "), ";
			}
			cerr << endl;
		}
	}
};

template<class T>
T string_to_digits(std::string& str)
{
	T value;
	std::string parsedStr;
	std::string::const_iterator iterator;
	for(iterator = str.begin(); iterator != str.end(); iterator++)
		if((*iterator) != ',')
			parsedStr += *iterator;
	std::istringstream myFloat(parsedStr);
	myFloat >> value;
	return value;
}

template<class T>
void tokenize(string& str, vector<T>& tokens, const string& delimiters)
{
    size_t lastPos = str.find_first_not_of(delimiters, 0);
    size_t pos = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
    	string temp = str.substr(lastPos, pos - lastPos);
        tokens.push_back(string_to_digits<T>(temp));
        lastPos = str.find_first_not_of(delimiters, pos);
        pos = str.find_first_of(delimiters, lastPos);
    }
}

bool validMatrix(lawnDS& lawn, vector<int>& largestRowValue, vector<int>& largestColValue)
{
	bool flag = true;
	for(map<int, vector<pair<int, int> > >::reverse_iterator itr = lawn.heights.rbegin(); itr != lawn.heights.rend(); ++itr) {
		int value = itr->first;
		for(vector<pair<int, int> >::iterator itr2 = itr->second.begin(); itr2 != itr->second.end(); ++itr2) {
			int row = itr2->first;
			int col = itr2->second;
			if(!(value == largestRowValue[row] || value == largestColValue[col]))
				flag = false;
		}
		cerr << endl;
	}
	return flag;
}

string matrize(vector<string> input, int row, int col)
{
	lawnDS list;

	boost::numeric::ublas::matrix<int> m (100, 100);
	vector<int> largestRowValue, largestColValue;

	vector<string>::iterator itr = input.begin(), itrEnd = input.end();
	for(unsigned i = 0; i < row && itr != itrEnd && i < m.size1(); ++i, ++itr) {
		vector<int> tokens;
		string delim = " ";
		tokenize(*itr, tokens, delim);

		int max = -1;
		for (unsigned j = 0; j < m.size2() && j < tokens.size(); ++ j) {
			m (i, j) = tokens[j];
			list.insert(tokens[j], i, j);
			if(tokens[j] > max)
				max = tokens[j];
		}
		largestRowValue.push_back(max);
	}

	for(unsigned j = 0; j < m.size2() && j < col; ++ j) {
		int max = -1;
		for(unsigned i = 0; i < m.size1() && i < row; ++ i) {
			if(m(i, j) > max)
				max = m(i, j);
		}
		largestColValue.push_back(max);
	}
/*
	cerr << "largest Row value" << endl;
	for(vector<int>::iterator itr = largestRowValue.begin(); itr != largestRowValue.end(); ++itr)
		cerr << *itr << ", ";
	cerr << endl;
	cerr << "largest Col value" << endl;
	for(vector<int>::iterator itr = largestColValue.begin(); itr != largestColValue.end(); ++itr)
		cerr << *itr << ", ";
	cerr << endl;

	for(unsigned i = 0; i < m.size1() && i < row; ++ i) {
		for(unsigned j = 0; j < m.size2() && j < col; ++ j)
			cerr << m (i, j) << " ";
		cerr << endl;
	}
*/
	//list.print();
	if(validMatrix(list, largestRowValue, largestColValue))
		return "YES";
	else
		return "NO";
}

int main() {
	ofstream* output;
	string filename = "input.in";
	string line;
	std::ifstream ifs(filename.c_str());
	string output_file = "output.op";
	output = new ofstream(output_file.c_str());

	int T = 0, testCase = 1;
	if ( ifs.is_open() ) {
		if( !ifs.eof() ) {
			getline( ifs, line );
			T = string_to_digits<int>(line);
		}
		for(int i = 0; !ifs.eof() && T > 0; i++, testCase++, T-- ) {
			getline( ifs, line );
			vector<int> tokens;
			string delim = " ";
			tokenize(line, tokens, delim);
			int row = tokens[0], col = tokens[1];
			vector<string> matrix;
			for(int j = 0; j < row; ++j){
				getline( ifs, line );
				matrix.push_back(line);
			}
			*output << "Case #" << testCase << ": " << matrize(matrix, row, col) << endl;
		}
	}
	output->close();
	return 0;
}
