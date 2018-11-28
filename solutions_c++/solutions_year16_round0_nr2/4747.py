#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int solve(const string& s) {
	string compressed;
	compressed.push_back(s[0]);
	for (int i = 1; i < s.size(); ++i)
		if (s[i - 1] != s[i]) compressed.push_back(s[i]);
	return compressed.size() + (compressed.back() == '+' ? -1 : 0);
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int c;
	fin >> c;
	for (int tc = 1; tc <= c; ++tc) {
		string s;
		fin >> s;
		fout << "Case #" << tc << ": " << solve(s) << endl;
	}
}