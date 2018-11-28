#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::string getLast(const std::string& input) {
	std::string result;
	for(auto it = input.begin(); it != input.end(); it++) {
		char curChar = *it;
		if(curChar >= result[0]) result = curChar + result;
		else result.push_back(curChar);
	}
	return result;
}

int main(int argc, char const *argv[]) {
	std::fstream inFile(argv[1], std::fstream::in);
	std::fstream outFile("result", std::fstream::out);
	int testSize;
	inFile >> testSize;
	for(int i = 0; i < testSize; ++i) {
		std::string input;
		inFile >> input;
		outFile << "Case #" << (i+1) << ": " << getLast(input) << std::endl;
	}
}
