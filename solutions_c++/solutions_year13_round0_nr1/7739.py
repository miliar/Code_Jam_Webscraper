#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool isGood(char pm, char c) {
	return ((pm == c) || (pm == 'T'));
}

bool isFour(char z, char a, char b, char c, char d) {
	return (isGood(a, z) && isGood(b, z) && isGood(c, z) && isGood(d, z));
}

bool isWin(char** pm, char c) {
	for(int i=0; i<4; i++) {
		if(isFour(c, pm[i][0], pm[i][1], pm[i][2], pm[i][3])) {
			return true;
		}
		if(isFour(c, pm[0][i], pm[1][i], pm[2][i], pm[3][i])) {
			return true;
		}
	}
	if(isFour(c, pm[0][0], pm[1][1], pm[2][2], pm[3][3])) {
		return true;
	}
	if(isFour(c, pm[0][3], pm[1][2], pm[2][1], pm[3][0])) {
		return true;
	}
	return false;
}

bool isChar(char** pm, char c) {
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(pm[i][j]==c) {
				return true;
			}
		}
	}
	return false;
}

string processing(char** pmatrix) {
	if(isWin(pmatrix,'X')) {
		return "X won";
	}
	if(isWin(pmatrix,'O')) {
		return "O won";
	}
	if(!isChar(pmatrix, '.')) {
		return "Draw";
	}
	return "Game has not completed";
}

int main () {
	int cnt;
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	char** matrix = new char*[4];
	for(int i=0; i<4; i++) {
		matrix[i] = new char[4];
	}
	
	string line;

	if(infile.is_open()) {
		infile >> cnt;
		for(int i=0; i<cnt; i++) {
			for(int j=0; j<4; j++) {
				infile >> line;
				for(int l=0; l<4; l++) {
					matrix[j][l] = line[l];
				}
			}
			outfile << "Case #" << i+1 << ": " << processing(matrix) << endl;
		}
		outfile.close();
		infile.close();
	} else {
		cout << "Unable to open file!" << endl;
	}
	
	if(matrix) {
		for(int i=0; i<4; i++) {
			if(matrix[i]) {
				delete [] matrix[i];
			}
		}
		delete [] matrix;
	}
	return 0;
}