#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream myfile ("B-large.in");
	ofstream outfile("B-large-answer.txt");
	int cases;
	myfile >> cases;
	for (int i = 0; i < cases; ++i) {
		int size = 0;
		int count = 0;
		string strn;
		myfile >> strn;
		size = strn.size();
		for (int j = 0; j < size - 1; ++j) {
			if (strn[j] != strn[j + 1]) {
				if (strn[j] == '+') {
					count += 2;
					while (strn[j + 1] == '-') {
						strn[j + 1] = '+';
						j++;
					}
				}
				else {
					count++;
				}
			}
		}
		if (count == 0 && strn[0] == '-') {
			count++;
		}
		outfile << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}