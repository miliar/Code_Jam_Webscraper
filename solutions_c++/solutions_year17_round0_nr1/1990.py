#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream fout("pancake.out");
	ifstream fin("pancake.in");
	int T;
	fin >> T;
	for (int i = 0; i < T; i++) {
		char cake[1010];
		int K;
		fin >> cake;
		fin >> K;
		int j = 0;
		bool possible = true;
		int count = 0;
		while (cake[j] && possible) {
			if (cake[j] == '-') {
				for (int k = 0; k < K; k++) {
					if (cake[j + k] == '-') {
						cake[j + k] = '+';
					}
					else if (cake[j + k] == '+') {
						cake[j + k] = '-';
					}
					else {
						possible = false;
					}
				}
				count++;
			}
			j++;
		}
		fout << "Case #" << i + 1 << ": ";
		if (possible) fout << count << endl;
		else fout << "IMPOSSIBLE" << endl;
	}
	system("pause");
}