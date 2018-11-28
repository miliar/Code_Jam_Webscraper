#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <limits>

using namespace std;

int main() {

	int testCase;

	ifstream input;
	input.open("A-small-attempt0.in");
	ofstream output("A-small-attempt0.out");
	input >> testCase;

	int firstAns, secondAns;
	vector<int> result;
	int first[4][4], second[4][4];

	for (int i=0; i<testCase; i++) {

		input >> firstAns;
		for(int j=0;j<4;j++){
			input >> first[j][0] >> first[j][1] >> first[j][2] >> first[j][3];
		}
		input >> secondAns;
		for(int j=0;j<4;j++){
			input >> second[j][0] >> second[j][1] >> second[j][2] >> second[j][3];
		}
		
		for (int k=0; k<4; k++) {
			for(int l=0; l<4; l++) {
				if(first[firstAns-1][k]==second[secondAns-1][l]) {
					result.push_back(first[firstAns-1][k]);
				}
			}
		}

		if(result.size()==0) {
			output << "Case #" << i+1 << ": Volunteer cheated!"<< endl;
			result.clear();
		}
		else if(result.size()>1) {
			output << "Case #" << i+1 << ": Bad magician!"<< endl;
			result.clear();
		}
		else {
			output << "Case #" << i+1 << ": " << result[0] << endl;
			result.clear();
		}
	}


	return 0;
}









