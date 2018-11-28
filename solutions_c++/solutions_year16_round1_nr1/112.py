#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

using ll = long long int;
ifstream fin("1.in");
ofstream fout("1.out");


int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		string str;
		fin >> str;
		string base = "";
		for (char c : str) {
			string a = c + base, b = base + c;
			if (a > b)
				base = a;
			else
				base = b;
		}
		fout << "Case #" << t << ": ";
		fout << base << endl;
	}
}
