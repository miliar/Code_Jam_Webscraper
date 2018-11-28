#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	for (int m = 0; m < T; m++) {
		string S;
		fin >> S;
		vector<bool> signs(S.size());
		for (int i = 0; i < S.size(); i++) {
			if (S[i] == '+') {
				signs[i] = true;
			}
			else {
				signs[i] = false;
			}
		}
		int answer = 0;
		bool before = signs[S.size() - 1];
		for (int i = S.size() - 1; i >= 0; i--) {
			if (i == S.size() - 1) {
				if (signs[i] == false) {
					answer++;
					continue;
				}
				else {
					continue;
				}
			}
			if (signs[i] != before) {
				answer++;
				before = signs[i];
			}
		}
		fout << "Case #" << m + 1 << ": " << answer << endl;
	}
    return 0;
}


