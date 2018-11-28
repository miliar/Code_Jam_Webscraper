#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <iomanip>
#include <vector>

using namespace std;

void flip(bool cakeBits[], int size, int start) {
 for (int i = start; i < size; ++i) {
 	cakeBits[i] = !cakeBits[i];
 }
}

int main() {
	ifstream inData("small.in");
	ofstream outData("output-small.txt");
	int num;
	inData >> num;
	for(int i = 0; i < num; i++) {
		string cake;
		inData >> cake;
		int size = cake.length();
		bool * cakeBits = new bool[size];;
		for (int j = size-1; j >= 0; --j) {
			if (cake[j] == '+') {
				cakeBits[(size-1)-j] = 1;
			} else {
				cakeBits[(size-1)-j] = 0;
			}
		}

		int flips = 0;
		for (int j = 0; j < size; ++j) {
			if (cakeBits[j] != 1) {
				flips++;
				flip(cakeBits, size, j);
			}
		}
		outData << "Case #" << i+1 << ": " << flips << endl;
	}
	return 0;
}

