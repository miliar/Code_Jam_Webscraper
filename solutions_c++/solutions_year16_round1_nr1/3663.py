#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main() {
	ifstream fin("A-large (2).in");
	ofstream fout("output.txt");
	int n;
	fin >> n;
	string s, result;
	for (int i = 1; i <= n; i++) {
		fin >> s;
		result += s[0];
		for (int j = 1; j < s.size(); j++) {
			if (s[j] >= result[0]) {
				result = s[j] + result;
			}
			else {
				result = result + s[j];
			}
		}
		fout << "Case #"<<i<<": " << result << "\n";
		result.clear();
	}
	return 0;
}