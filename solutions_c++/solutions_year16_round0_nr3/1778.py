#include <fstream>
#include <iostream>

int length = 32;
int maxIter = 500;

void printHalf(int counter, std::fstream& outFile) {
	outFile << '1';
	for(int i = 0; i < length / 2 - 2; ++i) {
		outFile << (counter % 2);
		counter /= 2;
	}
	outFile << '1';
}

long long getDivisor(int counter, int base) {
	long long result = 0;
	result = 1 * base;
	for(int i = 0; i < length / 2 - 2; ++i) {
		if(counter % 2) result += 1;
		counter /= 2;
		result *= base;
	}
	result += 1;
	return result;
}

int main(int argc, char const *argv[]) {
	std::fstream outFile("result", std::fstream::out);
	outFile << "Case #1:" << std::endl;
	int counter = 0;
	for(int i = 0; i < maxIter; ++i) {
		printHalf(counter, outFile);
		printHalf(counter, outFile);
		for(int i = 2; i <= 10; ++i) outFile << ' ' << getDivisor(counter, i);
		++counter;
		outFile << std::endl;
	}
}
