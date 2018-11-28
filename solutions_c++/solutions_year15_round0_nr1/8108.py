#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int T;
	fin >> T;
	for(int t = 0; t < T; t++){
		int max; string s;
		fin >> max >> s;

		unsigned int standing = 0, needed = 0;
		for(unsigned int i = 0; i < s.size(); i++){
			if(i > standing){
				needed += i - standing;
				standing = i;
			}
			standing += s[i]-'0';
		}
		fout << "Case #" << (t+1) << ": " << needed << endl;
	}
	return 0;
}
