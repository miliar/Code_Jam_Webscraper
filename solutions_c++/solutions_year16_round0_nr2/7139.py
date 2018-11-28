#include <iostream>
#include <string>
#include <fstream>
#include <ctime>

using namespace std;

int main() {
	clock_t tStart = clock();
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	
	int n;
	string s;
	fin >> n;
	for (int i = 0; i < n; ++i) {
		fin >> s;
		int index = 0;
		if (s[0] == '-') ++index;

		for (int j = 1; j < s.size(); ++j) {
			if (s[j] == '-' && s[j - 1] == '+') index += 2;
		}
		fout << "Case #" << (i + 1) << ": " << index << endl;
		cout << "Case #" << (i + 1) << ": " << index << endl;
	}

	printf("Time taken: %.2fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
	while (1);
	return 0;
}