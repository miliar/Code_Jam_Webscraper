#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

int getLast(unsigned int target) {
	bool hasDigit[10] = {false,};
	if(target == 0) return -1;
	int iter = 1;
	while(true) {
		unsigned int curTarget = (target * iter);
		while(curTarget) {
			hasDigit[curTarget % 10] = true;
			curTarget /= 10;
		}
		bool hasDigitSum = true;
		for(int i = 0; i < 10; ++i) hasDigitSum = hasDigitSum && hasDigit[i];
		if(hasDigitSum) return (target * iter);
		++iter;
	}
}

int main(int argc, char const *argv[]) {
	std::fstream inFile(argv[1], std::fstream::in);
	std::fstream outFile("result", std::fstream::out);
	int testSize;
	inFile >> testSize;
	for(int i = 0; i < testSize; ++i) {
		outFile << "Case #" << (i+1) << ": ";
		int input;
		inFile >> input;
		int result = getLast(input);
		if(result < 0) outFile << "INSOMNIA";
		else           outFile << result;
		outFile << std::endl;
	}
}
