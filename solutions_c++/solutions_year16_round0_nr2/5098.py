#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char ch(char a) {
	if (a == '-'){
		return '+';
	}
	else {
		return '-';
	}
}

void main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int T = 0;
	fin >> T;
	for (int k = 0; k < T; k++) {
		string res = "Case #" + to_string(k + 1) + ": ";
		string t;
		fin >> t;
		int r = 0;
		for (int i = t.size() - 1; i >= 0; i--) {
			if (t[i] == '-') {
				r++;
				for (int j = 0; j <= i; j++) {
					t[j] = ch(t[j]);
				}
			}
		}
		res += to_string(r);
		fout << res << endl;

	}
	fin.close();
	fout.close();
}