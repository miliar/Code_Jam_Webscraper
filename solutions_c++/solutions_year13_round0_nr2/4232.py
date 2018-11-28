#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <sstream>

using namespace std;

bool checkPattern(int pattern[100][100], int m, int n) {
	for(int i=0; i<m; i++) {
		for(int j=0; j<n; j++) {
			int hei = pattern[i][j];
			bool xdir = true;
			bool ydir = true;
			for(int k=0; k<m; k++) {
				if(hei < pattern[k][j]) {
					ydir = false;
				}
			}
			for(int k=0; k<n; k++) {
				if(hei < pattern[i][k]) {
					xdir = false;
				}
			}
			if(!xdir && !ydir) return false;
		}
	}
	return true;
}

int main() {
	string line;
	ifstream infile;
	ofstream outfile;
	int pattern[100][100];
	int m,n;
	bool result;
	infile.open("input.txt");
	outfile.open("output.txt");
	getline(infile, line);  // read test case number#
	int nCase = atoi(line.c_str());
	for(int i=0; i<nCase; i++) {
		getline(infile, line);
		istringstream is(line);
		is >> m;
		is >> n;
		for(int j=0; j<m; j++) {
			getline(infile, line);
			istringstream is(line);
			for(int k=0; k<n; k++) {
				is >> pattern[j][k];
			}
		}
		result = checkPattern(pattern, m, n);
		outfile << "Case #" << i+1 << ": ";
		if(result) outfile << "YES";
		else outfile << "NO";
		outfile << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
