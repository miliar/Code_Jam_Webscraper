#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int main() {

	ofstream fout ("output.out");
	ifstream fin ("A-small-attempt3.in");

	string nCases, row1, row2, number;
	int numCases, rowone, rowtwo, x = 1, result;
	int numbersone[4][4];
	int numberstwo[4][4];
	getline(fin, nCases, '\n');
	numCases = stoi(nCases);
	while(!fin.eof() || x < 100) {
		fin >> row1;
		rowone = stoi(row1);
		for(unsigned int i = 0; i < 4; i++) {
			for(unsigned int j = 0; j < 4; j++) {
				fin >> number;
				numbersone[i][j] = stoi(number);
			}
		}
		fin >> row2;
		rowtwo = stoi(row2);
		for(unsigned int i = 0; i < 4; i++) {
			for(unsigned int j = 0; j < 4; j++) {
				fin >> number; 
				numberstwo[i][j] = stoi(number);
			}
		}
		int nAppearances = 0;
		for(unsigned int i = 0; i < 4; i++) {
			for(unsigned int j = 0; j < 4; j++) {
				if(numbersone[rowone-1][i] == numberstwo[rowtwo-1][j]) {
					result = numbersone[rowone-1][i];
					nAppearances++;
				}
			}
		}
		if(nAppearances == 1) {
			fout << "Case #" << x << ": " << result << '\n';
		}
		else if(nAppearances > 1) {
			fout << "Case #" << x << ": " << "Bad magician!\n";
		}
		else {
			fout << "Case #" << x << ": " << "Volunteer cheated!\n";
		}
		x++;
	}
	return 0;
}