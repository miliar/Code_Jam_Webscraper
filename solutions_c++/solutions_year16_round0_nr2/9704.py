//============================================================================
// Name        : Asmall.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char *argv[]) {
	int T;
	string val;
	ifstream infile;
	infile.open(argv[1]);
	string p = "+";

	if (infile.is_open()) {

		infile >> T;

		int count;

		for (int i = 1; i <= T; i++) {
			count = 0;
			infile >> val;

			// push values onto boolean vector
			vector<bool> temp(val.length());
			int len = val.length();

//			cout << val << "[" << len << "]" << endl;

			// push into array
			for (int j = 0; j < len; j++) {
				string c = val.substr(j,1);
				if (c.compare(p) == 0)
					temp[j] = true;
				else
					temp[j] = false;
			}

//			cout << "Temp size: " << temp.size() << endl;

			int index = temp.size() - 1;

			while(index >= 0) {

				// Remove pancakes from consideration from bottom
				for (int j = index; j >= 0; j--) {
					if (temp[j]) {
						index--;
					} else {
						break;
					}
				}

				// flip remainder
				for (int j = 0; j <= index; j++)
					temp[j] = !temp[j];

				count++;
			}

			cout << "Case #" << i << ": " << count-1 << endl;
		}
	}
	else {
		cout << "Cannot open file " << endl;
	}
	infile.close();

	return 0;
}
