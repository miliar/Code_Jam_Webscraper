#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include <cassert>

using namespace std;


int main() {
	ifstream in;
	in.open("../Ain.txt");
	ofstream out;
	out.open("../Aout.txt");

	int T;
	in >> T;
	for (int icase = 1; icase <= T; ++icase) {
		out << "Case #" << icase << ": ";

		map<char, int> cnt;
		vector<int> res(10, 0);

		string s;
		in >> s;
		for (char c : s)
			++cnt[c];

		while (cnt['Z']) {
			++res[0];
			--cnt['Z'];
			--cnt['E'];
			--cnt['R'];
			--cnt['O'];
		}

		while (cnt['W']) {
			++res[2];
			--cnt['T'];
			--cnt['W'];
			--cnt['O'];
		}

		while (cnt['U']) {
			++res[4];
			--cnt['F'];
			--cnt['O'];
			--cnt['U'];
			--cnt['R'];
		}

		while (cnt['X']) {
			++res[6];
			--cnt['S'];
			--cnt['I'];
			--cnt['X'];
		}

		while (cnt['G']) {
			++res[8];
			--cnt['E'];
			--cnt['I'];
			--cnt['G'];
			--cnt['H'];
			--cnt['T'];
		}

		while (cnt['S']) {
			++res[7];
			--cnt['S'];
			--cnt['E'];
			--cnt['V'];
			--cnt['E'];
			--cnt['N'];
		}

		while (cnt['V']) {
			++res[5];
			--cnt['F'];
			--cnt['I'];
			--cnt['V'];
			--cnt['E'];
		}

		while (cnt['T']) {
			++res[3];
			--cnt['T'];
			--cnt['H'];
			--cnt['R'];
			--cnt['E'];
			--cnt['E'];
		}

		while (cnt['O']) {
			++res[1];
			--cnt['O'];
			--cnt['N'];
			--cnt['E'];
		}

		while (cnt['N']) {
			++res[9];
			--cnt['N'];
			--cnt['I'];
			--cnt['N'];
			--cnt['E'];
		}

		for (auto& p : cnt)
			assert(p.second == 0);

		for (int i = 0; i < 10; ++i)
			while (res[i]--)
				out << i;
		out << "\n";
	}
}