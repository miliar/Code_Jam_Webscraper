#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

bool pal(int value);
bool pal(string value);
bool square(int value);

int main() {
	int runs = 0;
	int min = 0;
	int max = 0;
	string str;
	stringstream ss;
	stringstream numb;
	ifstream infile;
	infile.open("C.in");
	infile >> runs;
	infile.ignore(100, '\n');
	
	for (int i = 0; i < runs; ++i) {
		getline(infile, str);
		ss.clear();
		ss.str("");
		ss << str;
		ss >> min >> max;
		
		int count = 0;
		for (int j = min; j <= max; j++) {
			numb.str("");
			numb << j;
			if (pal(numb.str()) && square(j)) count++;
			numb.clear();
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}

bool pal(int value) {
	stringstream str;
	str << value;
	return pal(str.str());
}
bool pal(string value) {
	string tmp(value);
	reverse(tmp.begin(), tmp.end());
	return (tmp == value);
}
bool square(int value) {
	// return sqrt(value*value)
	double d_sqrt = sqrt( value );
	int i_sqrt = d_sqrt;
	if ( (d_sqrt == i_sqrt) && pal(d_sqrt) ) {
		return true;
	}
	return false;
}