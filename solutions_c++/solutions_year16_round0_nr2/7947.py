#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

int main() {

	int T;
	int i, g, x, k, p;
	int SIZE;
	int flips;
	string S;

	ifstream inFile;
	inFile.open("B-large.in");

	ofstream outFile;
	outFile.open("output.txt");

	inFile >> T;

	for (i = 0; i < T; i++) {
		flips = 0;
		p = 0;
		inFile >> S;

		SIZE = S.length();

		vector<int> array;
		array.resize(SIZE);

		for (g = 0; g < SIZE; g++) {

			if (S.at(g) == '+')
				array[g] = 1;
			else if (S.at(g) == '-')
				array[g] = 0;

			if (SIZE == 1) {
				if (array[g] == 1)
					flips = 0;
			}

			if (g > 0) {
				if (array[g] != array[g - 1]) {
					if (array[g - 1] < array[g]) {
						for (k = 0; k < g; k++) {
							array[g - (k + 1)] = array[g];
						}
						flips++;
					}

					else if (array[g - 1] > array[g]) {
						for (k = 0; k < g; k++) {
							array[g - (k + 1)] = array[g];
						}
						flips++;
					}
				}
			}

		}

		for (x = 0; x < SIZE; x++){
			if (array[x] < 1)
				p++;
		}

		if (p == SIZE)
			flips++;


		outFile << "Case #" << i + 1 << ": " << flips << endl;
	}
	
	return 0;
}