#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

ifstream fin("pan.in");
ofstream fout("pan.out");

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		fin >> s;
		s.push_back('+');

		int ans = 0;
		for (int i = 0; i < s.size() - 1; i++)
			if (s[i] != s[i + 1])
				ans++;
		fout << "Case #" << t << ": " << ans << endl;
	}
}
