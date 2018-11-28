#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <map>


int main()
{
	std::ifstream infile("infile.txt");
	std::ofstream outfile("outfile.txt");

	int T = 0;
	infile >> T;
	for (int t = 1; t <= T; ++t) {
		int K, C, S;
		infile >> K >> C >> S;

		if (S * C < K) {
			outfile << "Case #" << t << ": IMPOSSIBLE" << std::endl;
			continue;
		}

		std::vector<long long> lenVec(C, 1);
		for (int i = 1; i < C; ++i) {
			lenVec[i] = lenVec[i - 1] * K;
		}

		std::vector<long long> posVec;
		int a = 0;
		while (a < K) {
			long long p = 0;
			for (int j = 0; j < C && a < K; ++j) {
				p += lenVec[j] * a;
				++a;
			}
			posVec.push_back(p);
		}

/*
		for (int i = 0; i < S; ++i) {
			const int a = i * C;
			long long p = 0;
			for (int j = 0; j < C; ++j) {
				p += lenVec[j] * std::(K-1, (a + j));
			}
			posVec.push_back(p);
		}
*/

		outfile << "Case #" << t << ":";
		for (int i = 0; i < posVec.size(); ++i) {
			outfile << ' ' << posVec[i] + 1;
		}
		outfile << std::endl;
	}

	return 0;
}
