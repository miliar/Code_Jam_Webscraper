#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int T = 0;
	fin >> T;
	for (int k = 0; k < T; k++) {
		string res = "Case #" + to_string(k + 1) + ": ";
		int K, C, S;
		fin >> K >> C >> S;
		if (C == 1) {
			if (S < K) {
				res += "IMPOSSIBLE";
			}
			else {
				for (int i = 1; i <= K; i++){
					res += to_string(i) + " ";
				}
			}
		}
		else {
			if (K == 1) {
				res += "1";
			}
			else if (S < K - 1) {
				res += "IMPOSSIBLE";
			}
			else {
				for (int i = 2; i <= K; i++){
					res += to_string(i) + " ";
				}
			}
		}
		fout << res << endl;

	}
	fin.close();
	fout.close();
}