#include <iostream>
#include <fstream>
#include <utility>
#include <string>

using namespace std;

int t;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.out");
	fin >> t;
	for (int i = 1; i <= t; i++) {
		int s;
		string str;
		fin >> s >> str;
		int res = 0, sum = 0;
		for (int j = 0; j <= s; j++) {
			if (str[j] - '0' == 0)
				continue;
			if (sum < j) {
				res += j - sum;
				sum += j - sum;
			}
			sum += str[j] - '0';
		}
		fout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}