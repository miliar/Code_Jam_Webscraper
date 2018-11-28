#include <iostream>
#include <fstream>
#include <string>
#include <bitset>

#define SIZE 101


int main() {
	std::ifstream fin;
	fin.open("input.txt");
	std::ofstream fout;
	fout.open("output.txt");

	int T;
	fin >> T;
	for (int i = 1; i <= T; ++i) {
		int K, C, S;
		fin >> K >> C >> S;
		fout << "Case #" << i << ": ";
		uint64_t block_size = std::pow(K, C - 1);
		if (C == 1) {
			if (S < K) {
				fout << "IMPOSSIBLE";
			} else {
				for (int b = 0; b < S; b++) {
					fout << b + 1 << " ";
				}
			}
		} else {
			for (int b = 0; b < S; b++) {
				fout << b * block_size + b + 1 << " ";
			}
		}
		fout << std::endl;
	}

	fin.close();
	fout.close();
	return 0;
}