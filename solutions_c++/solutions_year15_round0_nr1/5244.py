#include <fstream>
#include <iostream>
#include <cstdlib>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int main() {
	int tests, len;
	string s;
	fin >> tests;
	for(int test = 0; test < tests; ++test) {
		fin >> len >> s;
		int ans = 0, sum = 0;
		for(int i = 0; i < len + 1; ++i) {
			int x = s[i] - '0';
			if(x > 0) {
				if(sum < i) {
					ans += (i - sum);
					sum = i;
				}
				sum += x;
			}
		}
		fout << "Case #" << test + 1 << ": " << ans << endl;
	}
	return 0;
}
