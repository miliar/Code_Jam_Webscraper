#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream infile("A-large.in");
	ofstream myfile;
	myfile.open("large-answers.txt");
	int testcases;
	infile >> testcases;
	for (int i = 0; i < testcases; i++) {
		int Smax;
		infile >> Smax;

		string str;
		infile >> str;

		int numShy = str[0] - '0';
		int total = numShy;
		int toCall = 0;
		for (int j = 1; j <= Smax; j++) {
			if (total < j) {
				toCall += j - total;
				total = j + str[j] - '0';
			}	else {
				total += str[j] - '0';
			}
		}
		myfile << "Case #" << i+1 << ": " << toCall << endl;
	}
	myfile.close();
	return 0;
}
