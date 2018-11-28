#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int get_subs(string str, int j, int n, int last) {
	string left = str.substr(last, j - n + 1 - last);
	string right = str.substr(j+1);
	return (left.length() + 1)*(right.length() + 1);
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int T = 0;
	fin >> T;

	string consonants = "zxcvbnmsdfghjklpytrwq";

	string str;
	int n;
	for (int i = 0; i < T; ++i) {
		fin >> 	str >> n;
		int sum = 0;
		int last = 0;
		int cur_cons = 0;
		int j = 0;
		while (j < str.length()) {
			if (consonants.find(str[j]) != string::npos) {
				cur_cons++;
				if (cur_cons == n) {
					sum += get_subs(str, j, n, last);
					j = j - n + 1;
					last = j + 1;
					cur_cons = 0;
				}
			} else {
				cur_cons = 0;
			}
			++j;
		}
		fout << "Case #" << i + 1 << ": " << sum << endl;
	}
}