#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
	ifstream fin("A-small-attempt0.in");
	ofstream fout("out.txt");
	int T; fin >> T;
	string s, result;
	for (int i = 0; i < T; ++i) {
		fin >> s;
		//result = "";
		result = s[0];
		for (int j = 1; j < s.length(); ++j) {
			if (s[j] >= result[0])
				result = s[j] + result;
			else
				result += s[j];
		}
		fout << "Case #" << (i + 1) << ": " << result << endl;
	}
	cout << "OK";
	while (1);
	return 0;
}