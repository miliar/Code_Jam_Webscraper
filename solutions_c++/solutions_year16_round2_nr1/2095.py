#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <math.h>
#include <string>
#include <string.h>
#include <iomanip>

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)

using namespace std;

int main() {

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t, T, i, j, k, N;
	string s;
	int lc[26];
	int num[10];

	fin >> T;
	for1(t, T) {

		cout << "Case #" << t << ": ";
		fout << "Case #" << t << ": ";

		memset(lc, 0, sizeof(lc[0])*26);
		memset(num, 0, sizeof(num[0]) * 10);

		fin >> s;
		cout << s << " ";
		forn(i, s.length()) lc[(int)s[i] - 'A']++;

		forn(i, lc['Z' - 'A']) {
			num[0]++;
			lc['E' - 'A']--;
			lc['R' - 'A']--;
			lc['O' - 'A']--;
		}
		lc['Z' - 'A'] = 0;

		forn(i, lc['W' - 'A']) {
			num[2]++;
			lc['T' - 'A']--;
			lc['O' - 'A']--;
		}
		lc['W' - 'A'] = 0;

		forn(i, lc['U' - 'A']) {
			num[4]++;
			lc['F' - 'A']--;
			lc['R' - 'A']--;
			lc['O' - 'A']--;
		}
		lc['U' - 'A'] = 0;

		forn(i, lc['F' - 'A']) {
			num[5]++;
			lc['V' - 'A']--;
			lc['I' - 'A']--;
			lc['E' - 'A']--;
		}
		lc['F' - 'A'] = 0;

		forn(i, lc['X' - 'A']) {
			num[6]++;
			lc['S' - 'A']--;
			lc['I' - 'A']--;
		}
		lc['X' - 'A'] = 0;

		forn(i, lc['S' - 'A']) {
			num[7]++;
			lc['E' - 'A']--;
			lc['V' - 'A']--;
			lc['E' - 'A']--;
			lc['N' - 'A']--;
		}
		lc['S' - 'A'] = 0;

		forn(i, lc['O' - 'A']) {
			num[1]++;
			lc['E' - 'A']--;
			lc['N' - 'A']--;
		}
		lc['O' - 'A'] = 0;

		forn(i, lc['N' - 'A'] / 2) {
			num[9]++;
			lc['I' - 'A']--;
			lc['E' - 'A']--;
		}
		lc['N' - 'A'] = 0;

		forn(i, lc['G' - 'A']) {
			num[8]++;
			lc['E' - 'A']--;
		}

		forn(i, lc['E' - 'A'] / 2) {
			num[3]++;
		}

		forn(i, 10)
			forn(j, num[i]) {
			fout << i;
			cout << i;

		}

		cout << endl;
		fout << endl;
	}

	return 0;
}