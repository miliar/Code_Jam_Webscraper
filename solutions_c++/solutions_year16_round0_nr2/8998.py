#include<iostream>
#include<string>
#include<fstream>
using namespace std;

bool allHappy(string s) {
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			return false;
		}
	}
	return true;
}
int main() {
	int t;
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("output.txt");
	fin >> t;
	string s;
	for (int i = 1; i <= t; i++) {
		fin >> s;
		int count = 0;
		int j = s.size() - 1;
		while (true) {
			if (allHappy(s))	break;
			if (s[j] == '-') {
				for (int k = 0; k <= j; k++) {
					if (s[k] == '+') {
						s[k] = '-';
						continue;
					}
					else {
						s[k] = '+';
						continue;
					}
				}
				count++;
			}
			else {
				j = j - 1;
				continue;
			}
		}
		fout << "Case #" << i << ": " << count << "\n";
	}

	return 0;
}