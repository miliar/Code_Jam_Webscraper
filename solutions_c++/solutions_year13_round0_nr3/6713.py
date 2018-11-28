#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream> 

using namespace std;

bool isPalindrone(long num) {
	string result;
	ostringstream convert;
	convert << num;
	result = convert.str();
	for(short i = 0; i < result.length() / 2; i++) {
		if(result[i] != result[result.length()-1]) {
			return false;
		}
	}
	return true;
}

int main() {
	short numberCases;
	ifstream testFile("C-small-attempt0.in");
	ofstream output("output");
	testFile >> numberCases;
	printf("There are %d tests\n", numberCases);
	
	for(int i = 0; i < numberCases; i++) {
		long a, b, count = 0;
		testFile >> a >> b;
		for(long base = a; base <= b; base++) {
			long baseroot = sqrt(base);
			if(pow(baseroot, 2) == base && isPalindrone(base) && isPalindrone(baseroot)) {
				count++;
			}
		}
		output << "Case #" << i+1 << ": "<< count << endl;
	}
	testFile.close();
	output.close();
}
