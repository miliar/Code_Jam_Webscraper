#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

bool findCard(int answer1, vector<vector<int> > data1, int answer2, vector<vector<int> > data2);

int main(int argc, char*argv[]) {
	int counter = 0;
	int testCases = 0;


	ifstream readFile;
	readFile.open("A-small-attempt1.in");

	if (!readFile.is_open()) {
		cout << "Could not open input file" << endl;
	}
	else {
		if (counter == 0) {
			readFile >> testCases;
			counter++;
		}
		while (testCases != 0) {
			int answer1;
			readFile >> answer1;

			vector<vector<int> > data1;

			for (int i = 0; i < 4; i++) {
				string line1;
				vector<int> lineData1;
				int value;

				getline(readFile, line1);
				while (line1 == "") {
					getline(readFile, line1);
				}
				stringstream lineStream(line1);
				while (lineStream >> value)	{
					lineData1.push_back(value);
				}
				data1.push_back(lineData1);
			}

			int answer2;
			readFile >> answer2;
			
			vector<vector<int> > data2;

			for (int i = 0; i < 4; i++) {
				string line1;
				vector<int> lineData1;
				int value;

				getline(readFile, line1);
				while (line1 == "") {
					getline(readFile, line1);
				}
				stringstream lineStream(line1);
				while (lineStream >> value)	{
					lineData1.push_back(value);
				}
				data2.push_back(lineData1);
			}

			cout << "Case #" << counter << ": ";
			findCard(answer1, data1, answer2, data2);

			counter++;
			testCases--;
		}
	}
	system("pause");
}

bool findCard(int answer1, vector<vector<int> > data1, int answer2, vector<vector<int> > data2) {
	int ans = -1;
	vector<int> row1 = data1[answer1-1];
	vector<int> row2 = data2[answer2-1];

	for (int i = 0; i < row1.size(); i++) {
		if (find(row2.begin(), row2.end(), row1[i]) != row2.end()) {
			if (ans < 0) {
				ans = row1[i];
			}
			else {
				cout << "Bad magician!" << endl;
				return false;
			}
		}
	}

	if (ans < 0) {
		cout << "Volunteer cheated!" << endl;
		return false;
	}
	else {
		cout << ans << endl;
		return true;
	}
}