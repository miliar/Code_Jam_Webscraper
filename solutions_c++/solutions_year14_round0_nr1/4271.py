#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int getChar (ifstream & fin) {
	string line;
	getline (fin, line);
	char c = line[0];
	int result = c - '0';
	int size = line . length ();
	int i = 1;
	while (i < size) {
		result += (line[i] - '0');
		result *= 10;
		++i;
	}
	return result;
}

string getRow (ifstream & fin, int row) {
	int i;
	string line, aux;
	for (i = 0 ; i < row; ++i) {
		getline(fin, line);
	}
	for (i = 0; i < 4 - row; ++i) {
		getline (fin, aux);
	}
	return line;
}

vector<string> getCard (string row) {
	int i, size = row . length ();
	vector<string> result;
	string aux;
	for (i = 0; i < size; ++i) {
		if (row[i] == ' ') {
			result . push_back (aux);
			aux = "";
			continue;
		}
		aux += row[i];
	}
	result . push_back (aux);
	return result;
}



int main () {
	ifstream fin ("A-small-attempt3.in.txt");
	ofstream fout ("output.txt");
	int nbTest = getChar (fin);
	int i;
	for (i = 0; i < nbTest; ++i) {
		int firstAnswer = getChar (fin);
		string firstRowAnswer = getRow (fin, firstAnswer);
		vector<string> cards = getCard (firstRowAnswer);
		int secondAnswer = getChar (fin);
		string secondRowAnswer = getRow (fin, secondAnswer);
		vector<string> secondCards = getCard (secondRowAnswer);
		int k, j, goodJob = 0;
		string cardResult;
		for (k = 0; k < 4; ++k) {
			for (j = 0; j < 4; ++j) {
				if (cards[k] . compare(secondCards[j]) == 0) {++goodJob; cardResult = cards[k];}
			}
		}
		if (goodJob == 0) {
			fout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
		}
		else if (goodJob == 1) {
			fout << "Case #" << i+1 << ": " << cardResult << endl;
		}
		else {
			fout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
		}
	}
	fin . close ();
	fout . close ();
    return 0;
}
