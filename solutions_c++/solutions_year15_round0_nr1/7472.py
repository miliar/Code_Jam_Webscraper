#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <stdlib.h>

using namespace std;

bool hasEnough(int max, int* shyLevel) {
	int total = shyLevel[0];
	for (int i=1;i<=max;i++) {
		if (total >= i) {
			total += shyLevel[i];
		} else {
			return false;
		}
	}
	return true;
}

int main() {
	ifstream inputFile ("prob1.in");
	ofstream outputFile ("prob1.out");
	string myline;
	getline(inputFile, myline);
	stringstream ss(myline);
	int t;
	ss >> t;
	for (int i=0; i<t; i++) {
		getline(inputFile, myline);
		stringstream ss2(myline);
		int max;
		ss2 >> max;
		string people;
		ss2 >> people;
		int* shyLevel = new int[people.size()];
		for(int j=0;j<people.size();j++) {
			string temp = "";
			temp += people[j];
			shyLevel[j] = atoi(temp.c_str());
		}
		int counter = 0;
		while (!hasEnough(max, shyLevel)) {
			counter++;
			shyLevel[0]++;
		}
		outputFile << "Case #" << (i+1) << ": " << counter << endl;
		delete [] shyLevel;
	}
	inputFile.close();
	outputFile.close();
}