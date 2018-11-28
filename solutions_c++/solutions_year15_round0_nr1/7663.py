#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int CalculateMinNeed(int sMax, string digits) {
    int count = 0;
    int needed = 0;
    for (int i = 0; i <= sMax; ++i) {
	if (count >= i) {
	    count += (digits[i] - '0');
	} else {
	    needed += (i - count);
	    count = i + (digits[i] - '0');
	}
    }
    return needed;
}

int main() {

    int num = 0;
    string numTests;
    vector<int> needed;

    ifstream testFile("tests.txt");
    if (testFile.is_open()) {
	getline(testFile, numTests);
	num = stoi(numTests);
	for (int i = 1; i <= num; ++i) {
	    string sMax, digits;
	    getline(testFile, sMax, ' ');
	    getline(testFile, digits);
	    int minNeed = CalculateMinNeed(stoi(sMax), digits);
	    needed.push_back(minNeed);
	}
    	testFile.close();
    }

    ofstream outFile("result.txt");
    if (outFile.is_open()) {
	for (int i = 1; i <= num; ++i) {
	    outFile << "Case #" << i << ": " << needed[i-1] << endl;
	}
	outFile.close();
    }

    return 0;
}
