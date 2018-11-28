#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	
	int total;
	
	// get the total number of test cases
	fin >> total;
	if (total == 0 || total > 100) {
		cout << "Invalid Input parameter!" << endl;
		return -1;
	}

	int a1, a2;
	int cards[4][4];
	int firstRow[4];
	int secondRow[4];
	
	for (int i = 0; i < total; i++) {
		// the answer to the first question
		fin >> a1;
		
		// the first arrangement of the cards
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				fin >> cards[j][k];
				
				if (j == a1 - 1)
					firstRow[k] = cards[j][k];
			}
		}

		// the answer to the second question
		fin >> a2;
		
		// the second arrangement of the cards
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				fin >> cards[j][k];
				
				if (j == a2 - 1)
					secondRow[k] = cards[j][k];
			}
		}
		
		// find out how many cards are matched
		int numofmatch = 0;
		int numofcard = 0;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (firstRow[j] == secondRow[k]) {
					numofmatch++;
					numofcard = firstRow[j];
				}
			}
		}
		
		// print the result
		fout << "Case #" << i + 1 << ": ";
		if (numofmatch == 0)
			fout << "Volunteer cheated!" << endl;
		else if (numofmatch == 1)
			fout << numofcard << endl;
		else if (numofmatch > 1)
			fout << "Bad magician!" << endl;
	}
	
	return 0;
}