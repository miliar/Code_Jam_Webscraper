#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

const string FILE_NAME = "A-small-attempt0";

struct stabel {
	int row;
	int grid[4][4];
};

string proccess(struct stabel a, struct stabel b) {
	int n = 0, num = 0;
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(a.grid[a.row][i]==b.grid[b.row][j]) {
				n++;
				num = a.grid[a.row][i];
			}
		}
	}
	
	if(n==1) {
		ostringstream o;
		o << num;
		return o.str();
	}
	if(n>1) {
		return "Bad magician!";
	}
	return "Volunteer cheated!";
}

int main () {
	int cnt;

	string fin = FILE_NAME + ".in";
	ifstream infile(fin.c_str());
	string fout = FILE_NAME + ".out";
	ofstream outfile(fout.c_str());
	
	struct stabel a, b;
	
	if(infile.is_open()) {
		infile >> cnt;
		for(int i=0; i<cnt; i++) {
			infile >> a.row;
			a.row -= 1;
			for(int n=0; n<4; n++) {
				for(int m=0; m<4; m++) {
					infile >> a.grid[n][m];
				}
			}
			infile >> b.row;
			b.row -= 1;
			for(int n=0; n<4; n++) {
				for(int m=0; m<4; m++) {
					infile >> b.grid[n][m];
				}
			}
			
			outfile << "Case #" << i+1 << ": " << proccess(a, b) << endl;
		}
		outfile.close();
		infile.close();
	} else {
		cout << "Unable to open file!" << endl;
	}
	return 0;
}