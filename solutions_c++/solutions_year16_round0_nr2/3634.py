#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream fin("B-large.in");
	ofstream fout("output.txt");

	int t, ans;
	string s;
	fin >> t;

	for (int k = 1; k <= t; k++) {
		fin >> s;
		ans = (s[0] == '-');
		for (int i = 1; i < s.size(); i++) if (s[i] == '-' && s[i - 1] == '+') ans += 2;
		fout << "Case #" << k << ": " << ans << endl;
	}

	fin.close();
	fout.close();
	return 0;
}