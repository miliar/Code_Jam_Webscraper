#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

bool isSolved(string);

int main() {

	ifstream file;
	ofstream fileTwo;
	int iter = 0;


	file.open("test.dat");
	fileTwo.open("output.txt");

	file >> iter;

	for (int i = 0; i < iter; i++) {
		int currNum, itttt = 1, lastnum;
		file >> currNum;
		lastnum = currNum;
		string currStr = to_string(currNum);
		bool solved = false;
		if (currNum == 0) {
			fileTwo << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}
		

		solved = isSolved(currStr);

		while (!solved) {
			lastnum = currNum * itttt;
			currStr = currStr + to_string(lastnum);
			solved = isSolved(currStr);
			itttt++;
		}

		fileTwo << "Case #" << i + 1 << ": " << lastnum << endl;
	}

	return 0;
}

bool isSolved(string num) {
	bool solved = true;

	for (int i = 0; i < 10; ++i)
	{
		if (num.find(to_string(i)) == -1) {
			solved = false;
		}
	}

	return solved;
}



