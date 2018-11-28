#include <fstream>
#include <iostream>
#include <cstring>
#include <vector>

int T, K, C, S;

bool Calculate(std::vector<long long int> & results) {
	if (C == 1) {
		if(S < K) return false;
		for (int i = 1; i <= K; i++) results.push_back(i);
		return true;
	}

	for (int i = 1; i <= K; i++) results.push_back(1 + K*(i-1));
	for (int i = 3; i <= C; i++) {
		for (int j = 0; j < results.size(); j++) results[j] = (results[j] - 1)*K + 1;
	}
	return true;
}


int main() {
	std::ifstream fin("D-small-attempt1.in");
	std::ofstream fout("output.out");

	if(!fin.is_open() || !fout.is_open()) return 1;
	fin >> T;
//	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int num = 0;
		fin >> K >> C >> S;
//		scanf("%d%d%d", &K, &C, &S);
//		printf("%d: %d %d %d\n", t, K, C, S);

		std::vector<long long int> results;
		bool imp = Calculate(results);

		fout << "Case #" << t << ": ";

		if (imp == false || results.size() == 0) fout << "IMPOSSIBLE";
		else {
			for (int i = 0; i < results.size(); i++) {
//				printf("%lld ", results[i]);
				fout << results[i] << " ";
			}
		}
		fout << '\n';
//		printf("\n");
	}
}