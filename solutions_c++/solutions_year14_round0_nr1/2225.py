#include<fstream>
using namespace std;

int main() {
	int t, i, j, it, firstLine[4], secondLine[4], firstPos, secondPos, aux, nrMatches, card;
	ifstream fin("input.in");
	ofstream fout("output.out");
	fin >> t;
	for(it = 1; it <= t; it++) {
		fin >> firstPos;
		for(i = 1; i <= 4; i++) {
			if(i == firstPos) {
				fin >> firstLine[0] >> firstLine[1] >> firstLine[2] >> firstLine[3];
			} else {
				fin >> aux >> aux >> aux >> aux;
			}
		}

		fin >> secondPos;
		for(i = 1; i <= 4; i++) {
			if(i == secondPos) {
				fin >> secondLine[0] >> secondLine[1] >> secondLine[2] >> secondLine[3];
			} else {
				fin >> aux >> aux >> aux >> aux;
			}
		}

		nrMatches = 0;
		for(i = 0; i < 4; i++) {
			for(j = 0; j < 4; j++) {
				if(firstLine[i] == secondLine[j]) {
					nrMatches++;
					card = firstLine[i];
				}
			}
		}

		fout << "Case #" << it << ": ";
		if(nrMatches == 0) fout << "Volunteer cheated!";
		if(nrMatches > 1) fout << "Bad magician!";
		if(nrMatches == 1) fout << card;
		fout << "\n";
	}
	return 0;
}
