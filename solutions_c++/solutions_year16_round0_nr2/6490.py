#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

int main(void)
{
	ifstream fin("B-large.in");
	ofstream fout("out.txt");
	int testCase;
	fin >> testCase;
	for (int test = 0; test < testCase; ++test) {
		fout << "Case #" << test + 1 << ": ";
		string s;
		fin >> s;
		auto it = s.begin();
		auto beforeIt = it;
		++it;
		int flipped = 0;
		while (it != s.end()) {
			if (*beforeIt != *it)
				++flipped;
			beforeIt = it;
			++it;
		}
		if (*beforeIt == '-') ++flipped;
		//cout << flipped << endl;
		fout << flipped << endl;
	}
	fin.close();
	fout.close();

	return 0;
}