#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int T = 0;
	char c;
	int S;
	int ans = 0;
	fin >> T;
	string l;
	for (int k = 0; k < T; k++) {
		int cnt = 0;
		ans = 0;
		fin >> S;
		for (int i = 0; i < S+1; i++) {
			fin >> c;
			if (cnt < i) {ans += i-cnt; cnt = i;}
			cnt += c - '0';
		}
		fout << "Case #" << k+1 << ": " << ans << endl;
		getline(fin,l);
	}
	
	return 0;
}
