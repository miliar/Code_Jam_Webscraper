#include <iostream>
#include <fstream>
using namespace std;

int main() {
	// your code goes here
	ofstream outfile;
	ifstream infile ("B.in");
	outfile.open("B.out");
	int T;
	infile >> T;
	for (int i = 0; i < T; i++){
		string input;
		infile >> input;
		int counter = 0;
		char before;
		before = input[0];
		if (before == '-')counter++;
		for (int j = 1; j < input.size(); j++){
			if (before=='+' && input[j] == '-'){
				counter+=2;
			}
			before = input[j];
		}
		outfile << "Case #" << (i+1) << ": " << counter << endl;
	}
	outfile.close();
	infile.close();
	return 0;
}
