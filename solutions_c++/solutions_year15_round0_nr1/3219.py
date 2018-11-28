#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

ifstream fin ("A-large.in");
ofstream fout ("A-large.out");

int T, N;

int main() {
	fin >> T;

	for (int t = 1; t <= T; ++t) {
		fin >> N;
		int invitees = 0;
		char ovating_num_c;
		fin >> ovating_num_c;
		int ovating_num = ovating_num_c - '0';
		for (int n = 1; n <= N; ++n) {
			char shy_n;
			fin >> shy_n;
			shy_n -= '0';
			if (n > ovating_num) {
				invitees += n - ovating_num;
				ovating_num = n;
			}
			ovating_num += shy_n;
		}
		fout << "Case #" << t << ": " << invitees << endl;
	}
	return 0;
}
