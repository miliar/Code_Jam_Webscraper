#include <bits/stdc++.h>

std::ifstream fin("A-large.in");
std::ofstream fout("ff2.out");

int main() {

	int T;
	fin >> T;

	for (int TEST = 0; TEST < T; ++TEST)
	{
		int sMax;
		fin >> sMax;
		std::string s;
		fin >> s;
		//fout << s << "\n";
		int rs = 0;
		int cur = (int)s[0] - 48;
		for (int i = 1; i <= sMax + 1; ++i) {
			if (cur < i) {
				rs += i - cur;
				cur += i - cur;
			}
			cur += (int)s[i] - 48;
		}
		fout << "Case #" << TEST + 1 << ": " << rs << "\n";
	}
	return 0;
}