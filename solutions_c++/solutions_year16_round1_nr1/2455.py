#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

string findlast(string word) {
	string last;
	last.push_back(word[0]);
	for(int i=1; i<(int)word.size(); i++) {
		if(word[i]<last[0]) {
			last.push_back(word[i]);
		}
		else {
			string top;
			top.push_back(word[i]);
			last.insert(0, top);
		}
	}
	return last;
}

int main() {

	int T;
	fin >> T;
	for(int t=1; t<=T; t++) {
		string word;
		fin >> word;
		string last = findlast(word);
		fout << "Case #" << t << ": " << last << endl;
	}

	return 0;
}

