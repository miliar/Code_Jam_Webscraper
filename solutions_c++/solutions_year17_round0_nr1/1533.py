// q1.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <cstdint>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int64_t solve(vector<short> bits, size_t K) {
	int64_t i = bits.size() - 1;
	int64_t res = 0;
	
	while (i >= 0) {
		if (bits[i] == 1) {
			if (i < K - 1) {
				return -1; // IMPOSSIBLE
			}
			else {
				res++;
				for (size_t j = 0; j < K; j++) {
					bits[i - j] = 1 - bits[i - j];
				}
			}
		}
		i--;
	}

	return res;
}

int main()
{
	ifstream inFile;
	inFile.open("..\\..\\A-large.in");
	ofstream outFile;
	outFile.open("..\\..\\A-large.out");

	size_t T;
	inFile >> T;
	for (size_t i = 0; i < T; i++) {
		string S;
		size_t K;
		inFile >> S;
		inFile >> K;

		vector<short> bits;
		for (size_t i = 0; i < S.length(); i++) {
			bits.push_back(S[i] == '-' ? 1 : 0);
		}

		int64_t res = solve(bits, K);
		if (res != -1) {
			outFile << "Case #" << (i + 1) << ": " << res << endl;
		}
		else {
			outFile << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << endl;
		}
	}

	outFile.close();
	inFile.close();
	return 0;
}

