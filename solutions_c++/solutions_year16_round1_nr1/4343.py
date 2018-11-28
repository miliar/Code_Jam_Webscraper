#include<iostream>
#include<string>
#include<vector>
#include<fstream>

using namespace std;

int main() {

	int T;
	string S;
	int i, g, h, n;
	int SIZE;
	int ex;

	ifstream inFile;
	inFile.open("A-large.in");

	ofstream outFile;
	outFile.open("output.txt");
	
	inFile >> T;

	for (i = 0; i < T; i++) {
		string M;
		inFile >> S;	

		SIZE = S.length();

		vector<int> array;
		array.resize(SIZE);

		for (g = 0; g < SIZE; g++) {

			if (g == 0)
				array[g] = S.at(g);

			else if (g > 0) {
				if ((array[0] < S.at(g)) || (array[0] == S.at(g))) {
					int incr = 0;
					for (h = 0; h < g; h++) {
						incr++;
						array[g - (incr - 1)] = array[g - incr];
					}
					array[0] = S.at(g);
				}
				else 
					array[g] = S.at(g);
			}
		}

		for (n = 0; n < SIZE; n++) {
			M += array[n];
		}
		
		outFile << "Case #" << i + 1 << ": " << M << endl;

	}

	return 0;

}