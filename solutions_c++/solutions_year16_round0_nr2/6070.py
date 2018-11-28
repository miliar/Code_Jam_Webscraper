#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");

int T;

int main()
{
	fin >> T;
	for(int i = 1; i <= T; i++) {
		fout << "Case #" << i << ": ";
		string s;
		fin >> s;
		int ans = 0;
		for(int j = 1; j < s.length(); j++) {
			if(s[j] != s[j - 1]) {
				ans++;
			}
		}
		if(s[s.length() - 1] == '-') {
			ans++;
		}
		fout << ans << "\n";
	}
	return 0;
}