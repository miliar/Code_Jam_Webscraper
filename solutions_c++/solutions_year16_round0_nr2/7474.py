#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <queue>
#include <fstream>

using namespace std;

void change(string& s, int i) {
	for (int j = 0; j < i; ++j) s[j] = (s[j] == '-' ? '+' : '-');
}

int main() {
	ifstream fin("B-large.in");
	ofstream fout("A.txt");
	int t;
	fin >> t;
	for (int i = 1; i <= t; ++i) {
		int ans=0;
		string s;
		fin >> s;
		int p = 0;
		while (p < s.size()-1) {
			if (s[p] != s[p + 1]) {
				change(s, p + 1);
				++ans;
			}
			++p;
		}
		if (s[0] == '-') ++ans;
		fout << "Case #" << i << ": " << ans << endl;
	}
	//cin.get(); cin.get();
	return 0;
}