#include <iostream>
#include <fstream>

#include <string>
#include <sstream>
#include <cstdlib>
#include "math.h"
#include <vector>
#include <stack>
#include <map>


using namespace std;

// open input and output files
// pre: user is prepared to enter file names at the keyboard
// post: files have been opened
void openFiles(ifstream &infile, ofstream &outfile);




int main()
{
	
	ifstream infile;
	ofstream outfile;
	openFiles(infile, outfile);

	cout << "Reading the input file..." << endl;

	size_t cases;
	infile >> cases;
	string s;
	size_t arr[10];
	for (int y = 0; y < 10; y++) {
		arr[y] = 0;
	}
	for (size_t x = 1; x <= cases; x++) {
		outfile << "Case #" << x << ": ";
		infile >> s;
		cout << s << " ";

		while (s.find('Z') != string::npos) {
			arr[0]++;
			s.erase(s.find('Z'),1);
			s.erase(s.find('E'),1);
			s.erase(s.find('R'),1);
			s.erase(s.find('O'),1);
		}
		while (s.find('X') != string::npos) {
			arr[6]++;
			s.erase(s.find('S'), 1);
			s.erase(s.find('I'), 1);
			s.erase(s.find('X'), 1);
		}
		while (s.find('S') != string::npos) {
			arr[7]++;
			s.erase(s.find('S'), 1);
			s.erase(s.find('E'), 1);
			s.erase(s.find('V'), 1);
			s.erase(s.find('E'), 1);
			s.erase(s.find('N'), 1);
		}
		while (s.find('V') != string::npos) {
			arr[5]++;
			s.erase(s.find('F'), 1);
			s.erase(s.find('I'), 1);
			s.erase(s.find('V'), 1);
			s.erase(s.find('E'), 1);
		}
		while (s.find('F') != string::npos) {
			arr[4]++;
			s.erase(s.find('F'), 1);
			s.erase(s.find('O'), 1);
			s.erase(s.find('U'), 1);
			s.erase(s.find('R'), 1);
		}
		while (s.find('G') != string::npos) {
			arr[8]++;
			s.erase(s.find('E'), 1);
			s.erase(s.find('I'), 1);
			s.erase(s.find('G'), 1);
			s.erase(s.find('H'), 1);
			s.erase(s.find('T'), 1);
		}
		while (s.find('S') != string::npos) {
			arr[7]++;
			s.erase(s.find('S'), 1);
			s.erase(s.find('E'), 1);
			s.erase(s.find('V'), 1);
			s.erase(s.find('E'), 1);
			s.erase(s.find('N'), 1);
		}
		while (s.find('H') != string::npos) {
			arr[3]++;
			s.erase(s.find('T'), 1);
			s.erase(s.find('H'), 1);
			s.erase(s.find('R'), 1);
			s.erase(s.find('E'), 1);
			s.erase(s.find('E'), 1);
		}
		while (s.find('W') != string::npos) {
			arr[2]++;
			s.erase(s.find('T'), 1);
			s.erase(s.find('W'), 1);
			s.erase(s.find('O'), 1);
		}
		while (s.find('O') != string::npos) {
			arr[1]++;
			s.erase(s.find('O'), 1);
			s.erase(s.find('N'), 1);
			s.erase(s.find('E'), 1);
		}
		while (s.find('N') != string::npos) {
			arr[9]++;
			s.erase(s.find('N'), 1);
			s.erase(s.find('I'), 1);
			s.erase(s.find('N'), 1);
			s.erase(s.find('E'), 1);
		}
		for (int y = 0; y < 10; y++) {
			for (size_t z = 0; 0 < arr[y]; z++) {
				outfile << y;
				arr[y]--;
			}
		}
		outfile << endl;
	}

	// close the files
	infile.close();
	outfile.close();
	cout << "Press enter to exit:" << endl;
	cin.get();
	cin.get();
}


// open input and output files
// pre: user is prepared to enter file names at the keyboard
// post: files have been opened
void openFiles(ifstream &infile, ofstream &outfile)
{

	// open input data file
	string inFileName;
	cout << "Enter the name of the input file: ";
	cin >> inFileName;
	infile.open(inFileName.c_str());
	if (infile.fail()) {
		cout << "Error opening input data file" << endl;
		char junk;
		cout << "press enter to exit";
		junk = cin.get();
		junk = cin.get();
		exit(1);
	}

	// open output data file
	string outFileName;
	cout << "Enter the name of the output file: ";
	cin >> outFileName;
	outfile.open(outFileName.c_str());
	if (outfile.fail()) {
		cout << "Error opening output data file" << endl;
		char junk;
		cout << "press enter to exit";
		junk = cin.get();
		junk = cin.get();
		exit(1);
	}

}