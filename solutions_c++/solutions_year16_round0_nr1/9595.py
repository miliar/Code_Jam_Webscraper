//============================================================================
// Name        : Asmall.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <algorithm>    // std::set_union, std::sort
#include <vector>       // std::vector
#include <set>

using namespace std;

int main(int argc, char *argv[]) {


	int T, val;

	ifstream infile;
	infile.open(argv[1]);

	if (infile.is_open()) {

		infile >> T;
		vector <int> allDigits;
		vector <int> tempDigits;
		int count;
		bool infinite = true;

		for (int i = 1; i <= T; i++) {
			infile >> val;
			infinite = false;
			allDigits.clear();
			count = 1;

			while (allDigits.size() < 10 && count < 100 && infinite == false) {
				int temp = val * count;
				tempDigits.clear();
				std::vector<int>::iterator it;
				//			cout << "Number: " << temp << endl;
				// Scrape digits into tempDigits
				while (temp >= 1) {
					tempDigits.push_back(temp % 10);
					temp /= 10;
				}

				// Punch to set to sort and remove duplicates and place back
				set <int> tempSet(tempDigits.begin(), tempDigits.end());
				tempDigits.assign(tempSet.begin(), tempSet.end());

				//			cout << "tempDigits: ";
				//			for (unsigned int j = 0; j < tempDigits.size(); j++)
				//				cout << tempDigits[j] << " ";
				//			cout << endl;

				// add to allDigits and punch to set and back to sort and remove duplicates
				for (unsigned int j = 0; j < tempDigits.size(); j++)
					allDigits.push_back(tempDigits[j]);

				//			cout << "allDigits: ";
				//			for (unsigned int j = 0; j < allDigits.size(); j++)
				//				cout << allDigits[j] << " ";
				//			cout << endl;

				set <int> tempSet2(allDigits.begin(), allDigits.end());
				allDigits.assign(tempSet2.begin(), tempSet2.end());

				//			cout << "allDigits: ";
				//			for (unsigned int j = 0; j < allDigits.size(); j++)
				//				cout << allDigits[j] << " ";
				//			cout << endl;

				count++;

				if (count == 99) {
					infinite = true;
				}
			}

			if (infinite)
				cout << "Case #" << i << ": INSOMNIA" << endl;
			else
				cout << "Case #" << i << ": " << val*(count-1) << endl;
		}
	}
	else {
		cout << "Cannot open file " << endl;
	}
	infile.close();

	return 0;
}
