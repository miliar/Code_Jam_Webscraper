#include <fstream>
#include <iostream>
#include <string>

int getCount(std::string& input) {
	int count = 0;
	input = input + '+';
	for(int i = 0; i < input.size() - 1; ++i) {
		if(input[i] != input[i + 1]) count++;
	}
	return count;
}

int main(int argc, char const *argv[]) {
	std::fstream inFile(argv[1], std::fstream::in);
	std::fstream outFile("result", std::fstream::out);
	int testSize;
	inFile >> testSize;
	for(int i = 0; i < testSize; ++i) {
		outFile << "Case #" << (i + 1) << ": ";
		std::string input;
		inFile >> input;
		outFile << getCount(input) << std::endl;
	}
}
