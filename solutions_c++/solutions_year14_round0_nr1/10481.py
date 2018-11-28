#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<int>* getRow(ifstream&, int);

int compareSet(vector<int>* s1, vector<int>* s2);

int main(int argc, char* argv[]) {
	if (argc > 1) {
		ifstream inputFile;
		inputFile.open(argv[1]);
		ofstream output;
		output.open("output.txt");

		int numCases;
		inputFile >> numCases;

		for (int i = 0; i < numCases; i++) {
			int rowNum1, rowNum2;
			inputFile >> rowNum1;

			vector<int>* set1 = getRow(inputFile, rowNum1);

			inputFile >> rowNum2;
			vector<int>* set2 = getRow(inputFile, rowNum2);

			int answer = compareSet(set1, set2);


			output << "Case #" << (i + 1) << ": ";
			if (answer == -1) {
				output << "Volunteer cheated!";
			}
			else if (answer == -2) {
				output << "Bad magician!";
			}
			else {
				output << answer;
			}
			output << endl;

			delete set1;
			delete set2;
		}

		inputFile.close();
		output.close();
	}
}

vector<int>* getRow(ifstream& inputStream, int rowNum) {
	vector<int>* ret = new vector<int>();

	for (int i = 0; i < 4; i++) {		
		for (int j = 0; j < 4; j++) {
			int num;
			inputStream >> num;
			if (i == rowNum - 1) {
				ret->push_back(num);
			}
		}			
	}

	return ret;
}

int compareSet(vector<int>* s1, vector<int>* s2) {
	int ans = -1;
	int numAnswers = 0;

	for (int i = 0; i < s1->size(); i++) {
		for (int j = 0; j < s2->size(); j++) {
			if (s1->at(i) == s2->at(j)) {
				ans = s1->at(i);
				numAnswers++;
				break;
			}
		}
	}

	if (numAnswers > 1)
		ans = -2;

	return ans;
}