#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <list>
using namespace std;


int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int c;
	fin >> c;
	for (int tc = 1; tc <= c; ++tc) {
		string S;
		fin >> S;
		list<char> output;
		output.push_back(S[0]);
		for (int i = 1; i < S.size(); ++i) {
			if (S[i] >= output.front()) output.push_front(S[i]);
			else output.push_back(S[i]);

		}
		fout << "Case #" << tc << ": ";
		list<char>::iterator it;
		for (it = output.begin(); it != output.end(); ++it) {
			fout << *it;
		}
		fout << endl;
	}
}