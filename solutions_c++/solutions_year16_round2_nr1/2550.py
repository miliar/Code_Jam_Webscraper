#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int* findDigit(std::string& input) {
	auto result = new int[10];
	for(int i = 0; i < 10; ++i) result[i] = 0;
	for(auto it = input.begin(); it != input.end(); ++it) {
		switch (*it) {
			case 'Z' : result[0]++; break;
			case 'W' : result[2]++; break;
			case 'X' : result[6]++; break;
			case 'U' : result[4]++; break;
			case 'O' : result[1]++; break;
			case 'R' : result[3]++; break;
			case 'F' : result[5]++; break;
			case 'S' : result[7]++; break;
			case 'H' : result[8]++; break;
			case 'I' : result[9]++; break;
		}
	}
	result[3] -= result[0];
	result[1] -= result[0];

	result[1] -= result[2];

	result[7] -= result[6];
	result[9] -= result[6];

	result[5] -= result[4];
	result[1] -= result[4];
	result[3] -= result[4];

	result[8] -= result[3];

	result[9] -= result[5];

	result[9] -= result[8];
	return result;
}

int main(int argc, char const *argv[]) {
	std::fstream inFile(argv[1], std::fstream::in);
	std::fstream outFile("result", std::fstream::out);
	int testSize;
	inFile >> testSize;
	for(int i = 0; i < testSize; ++i) {
		outFile << "Case #" << (i+1) << ": ";
		std::string input;
		inFile >> input;
		auto result = findDigit(input);
		for (int j = 0; j < 10; ++j) {
			for (int k = 0; k < result[j]; ++k) outFile << j;
		}
		delete[] result;
		outFile << std::endl;
	}
}