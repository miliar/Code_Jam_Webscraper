#include <iostream>
#include <string>
#include <set>
#include <fstream>
#include <ctime>

using namespace std;

int main() {
	clock_t tStart = clock();
	set<char> sc;
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int n; fin >> n;
	int value;

	for (int i = 0; i < n; ++i) {
		fin >> value;
		if (value != 0) {
			string s;
			if (sc.size() > 0)
				sc.clear();
			int number = value, iter = 0;
			while (iter < 1000 && sc.size() < 10) {
				s = to_string(number);
				for (auto &ch : s) {
					sc.insert(ch);
				}
				number += value;
				++iter;
			}
			fout << "Case #" << (i + 1) << ": " << value * iter << endl;
			cout << "Case #" << (i + 1) << ": " << value * iter << endl;
		}
		else {
			fout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
			cout << "Case #" << (i + 1) << ": INSOMNIA" << endl;
		}
	}

	printf("Time taken: %.2fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
	while (1);
	return 0;
}