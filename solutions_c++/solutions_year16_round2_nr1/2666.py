#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
#include <bitset>
#include <time.h>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <assert.h>

using namespace std;


int t;
int cnt[10];
int alpha_cnt[26];

void clear() {
	memset(cnt, 0, sizeof(int) * 10);
	memset(alpha_cnt, 0, sizeof(int) * 26);
}


int main() {
	ifstream fin("A-large.in", ifstream::in);  // TODO
	ofstream fout("result.out", ofstream::out);
	fin >> t;
	//cin >> t;
	string s;
	for (int i = 0; i < t; ++i) {
		clear();
		//cin >> s;
		fin >> s;
		for (int j = 0; j < s.size(); ++j) {
			alpha_cnt[s[j] - 'A'] += 1;
		}
		cnt[0] = alpha_cnt['Z' - 'A'];
		alpha_cnt['Z' - 'A'] -= cnt[0];
		alpha_cnt['E' - 'A'] -= cnt[0];
		alpha_cnt['R' - 'A'] -= cnt[0];
		alpha_cnt['O' - 'A'] -= cnt[0];
		cnt[2] = alpha_cnt['W' - 'A'];
		alpha_cnt['T' - 'A'] -= cnt[2];
		alpha_cnt['W' - 'A'] -= cnt[2];
		alpha_cnt['O' - 'A'] -= cnt[2];
		cnt[4] = alpha_cnt['U' - 'A'];
		alpha_cnt['F' - 'A'] -= cnt[4];
		alpha_cnt['O' - 'A'] -= cnt[4];
		alpha_cnt['U' - 'A'] -= cnt[4];
		alpha_cnt['R' - 'A'] -= cnt[4];
		cnt[6] = alpha_cnt['X' - 'A'];
		alpha_cnt['S' - 'A'] -= cnt[6];
		alpha_cnt['I' - 'A'] -= cnt[6];
		alpha_cnt['X' - 'A'] -= cnt[6];
		cnt[8] = alpha_cnt['G' - 'A'];
		alpha_cnt['E' - 'A'] -= cnt[8];
		alpha_cnt['I' - 'A'] -= cnt[8];
		alpha_cnt['G' - 'A'] -= cnt[8];
		alpha_cnt['H' - 'A'] -= cnt[8];
		alpha_cnt['T' - 'A'] -= cnt[8];

		cnt[3] = alpha_cnt['H' - 'A'];
		alpha_cnt['T' - 'A'] -= cnt[3];
		alpha_cnt['H' - 'A'] -= cnt[3];
		alpha_cnt['R' - 'A'] -= cnt[3];
		alpha_cnt['E' - 'A'] -= cnt[3] * 2;
		cnt[5] = alpha_cnt['F' - 'A'];
		alpha_cnt['F' - 'A'] -= cnt[5];
		alpha_cnt['I' - 'A'] -= cnt[5];
		alpha_cnt['V' - 'A'] -= cnt[5];
		alpha_cnt['E' - 'A'] -= cnt[5];
		cnt[7] = alpha_cnt['S' - 'A'];
		alpha_cnt['S' - 'A'] -= cnt[7];
		alpha_cnt['V' - 'A'] -= cnt[7];
		alpha_cnt['N' - 'A'] -= cnt[7];
		alpha_cnt['E' - 'A'] -= cnt[7] * 2;

		cout << cnt[0] << ", " << cnt[2] << " " << cnt[4] << endl;
		cnt[1] = alpha_cnt['O' - 'A'];
		cnt[9] = alpha_cnt['I' - 'A'];

		vector<char> result;
		for (int j = 0; j < 10; ++j) {
			cout << "cnt " << j << ": " << cnt[j] << endl;
			for (int k = 0; k < cnt[j]; ++k) {
				result.push_back(j + '0');
			}
		}
		cout << "Case #" << (i + 1) << ": ";
		fout << "Case #" << (i + 1) << ": ";
		for (int j = 0; j < result.size(); ++j) {
			cout << result[j];
			fout << result[j];
		}
		cout << endl;
		fout << endl;
	}
	return 0;
}
