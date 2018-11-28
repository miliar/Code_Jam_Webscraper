//============================================================================
// Name        : FairSquare.cpp
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
#include <algorithm>

#include <cmath>
#include <math.h>

using namespace std;

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

template<typename T>
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

bool isPalindrome(unsigned long long x) {
  if (x < 0) return false;
  unsigned long long div = 1;
  while (x / div >= 10) {
    div *= 10;
  }
  while (x != 0) {
  unsigned long long l = x / div;
  unsigned long long r = x % 10;
    if (l != r) return false;
    x = (x % div) / 10;
    div /= 100;
  }
  return true;
}

bool is_perfect_square(unsigned long long n) {
    if (n < 0)
        return false;
    unsigned long long root(round(sqrt(n)));
    return n == root * root;
}

int compute(string line)
{
	vector<unsigned long long> tokens;
	string delim = " ";
	tokenize(line, tokens, delim);
	vector<unsigned long long>::iterator iterator = tokens.begin();
	int start = tokens[0], end = tokens[1];

	unsigned long long start_sqrt, end_sqrt = sqrt(end);
	if(is_perfect_square(start))
		start_sqrt = sqrt(start);
	else
		start_sqrt = sqrt(start) + 1;

	vector<unsigned long long> elements;
	for(unsigned long long i = start_sqrt; i <= end_sqrt; ++i){
		if(isPalindrome(i)){
			unsigned long long square = i*i;
			if(isPalindrome(square))
				elements.push_back(square);
		}
	}

	cerr << "Fair Sq palindroms bw " << start << " & " << end << ":\n";
	for(vector<unsigned long long>::iterator itr = elements.begin(); itr != elements.end(); ++itr)
		cerr << *itr << endl;
	return elements.size();
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
			*output << "Case #" << testCase << ": " << compute(line) << endl;
		}
	}
	output->close();
	return 0;
}
