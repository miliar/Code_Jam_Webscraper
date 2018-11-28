//Farhan Javed - NUCES - Pakistan

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream inFile;
	inFile.open("A-small-attempt4.in");
	ofstream outputFile;
	outputFile.open("answer.txt");
	int **ptr;
	int x = 0, line_number, reps = 0, count = 0, number = 0;
	int *choose = new int[4];
	ptr = new int*[4];
	for (int i = 0; i < 4; ++i)
		ptr[i] = new int;
	inFile >> reps;
	while (x < reps) {
		inFile >> line_number;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				inFile >> ptr[i][j];
		for (int i = 0; i < 4; ++i)
			choose[i] = ptr[line_number - 1][i];
		inFile >> line_number;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				inFile >> ptr[i][j];
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; j++)
				if (choose[i] == ptr[line_number - 1][j]) {
					count++;
					number = choose[i];
				}
		if (count == 1)
			outputFile << "Case #" << x + 1 << ": " << number << endl;
		else if (count == 0)
			outputFile << "Case #" << x + 1 << ": Volunteer cheated!" << endl;
		else
			outputFile << "Case #" << x + 1 << ": Bad magician!" << endl;
		x++;
		count = 0;
	}
	outputFile.close();
	return 0;
}
