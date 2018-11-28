#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream fin("A.txt");
	ofstream fout("A_out.txt");

	int t;
	fin >> t;
	for (int i = 1; i <= t; i++) {
		int s;
		string str;
		fin >> s >> str;

		int stand = 0, invite = 0;
		for (int j = 0; j < str.length(); j++) {
			int person = str[j] - '0';
			if (person) {
				if (stand < j) {
					invite += j - stand;
					stand += j - stand;
				}
				stand += person;
			}
		}

		fout << "Case #" << i << ": " << invite << endl;
	}

	return 0;
}