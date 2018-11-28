#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
using namespace std;

int countFairSquare(unsigned long long int lower, unsigned long long int upper);

int main() {
	string inputFile, line;
    const char * iF;
    ifstream input;
    ofstream output;
    int cases, FaS;
	unsigned long long int lower, upper;
    
    cout << "Enter Input File: ";
    getline(cin, inputFile);
    iF = inputFile.c_str();
    input.open(iF);
    output.open("output.txt");
    if (!input.is_open()) {
        cout << "Failed to open input file\n";
        return -1;
    }
    if (!output.is_open()) {
        cout << "Failed to open output file\n";
        return -1;
    }
	input >> cases;
	for (int i = 1; i <= cases; i++) {
		input >> lower >> upper;
		FaS = countFairSquare(lower, upper);
		output << "Case #" << i << ": " << FaS;
		if (i < cases)
			output << "\n";
	}
	input.close();
	output.close();
}

string iToS(int number) {
	stringstream s;
	s << number;
	return s.str();
}

int isPal(unsigned long long int number) {
	string num  = iToS(number);
	int len, half;
	len = num.length();
	half = len/2;
	for (int i = 0; i < half; i++) {
		if (num[i] != num[len - (i+1)])
			return 0;
	}
	return 1;
}

int countFairSquare(unsigned long long int lower, unsigned long long int upper){
	int count = 0;
	unsigned long long int max = (unsigned long long int)sqrt(upper);
	for (unsigned long long int i = 1; i <= max; i++) {
		if (isPal(i)) {
			if ((i*i >= lower) && isPal(i*i))
				count++;
		}
	}
	return count;
}
	
