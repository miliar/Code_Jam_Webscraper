#include <iostream>
#include <fstream>
#include <string>
using namespace std;

unsigned long long int numCircles(unsigned long long int, unsigned long long int);

int main() {
    string inputFile, line;
    const char * iF;
    ifstream input;
    ofstream output;
    int cases;
	unsigned long long int r, t;
    
    cout << "Enter Input File: ";
    getline(cin, inputFile);
    iF = inputFile.c_str();
    input.open(iF);
    output.open("1a_Output.txt");
    if (!input.is_open()) {
        while (!input.is_open()) {
            cout << "Failed to open input file\n";
            input.open(iF);
        }
    }
    cout << "Input File Open\n";
    if (!output.is_open()) {
        while (!output.is_open()) {
            cout << "Failed to open output file\n";
            output.open("Lawnmower_Output.txt");
        }
    }
    cout << "Output File Open\n";
    getline(input, line);
    cases = atoi(line.c_str());
	for(int i = 1; i <= cases; i++) {
		input >> r;
		input >> t;
		output << "Case #" << i << ": " << numCircles(r, t);
		if( i < cases)
			output << "\n";
	}
	input.close();
	output.close();
	return 0;
}

unsigned long long int numCircles(unsigned long long int r, unsigned long long int t) {
	unsigned long long int paint = t;
	unsigned long long int rad = r;
	unsigned long long int count = 0;
	while (paint >= (((rad + 1) * (rad + 1)) - (rad * rad))) {
		count += 1;
		paint -= (((rad + 1) * (rad + 1)) - (rad * rad));
		rad += 2;
	}
	return count;
}
		
	
