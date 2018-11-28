//============================================================================
// Name        : 1b-a.cpp
// Author      : 
// Version     :
//============================================================================
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <string>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i < _a; ++i)

using namespace std;

int Remain = 0;
int letter[26];
string digits[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void takeDigit(int d, int times) {
	REP(i, digits[d].size()) {
		letter[digits[d][i] - 'A'] -= times;
	}
}

int main() {
	int T;
	string S;
	int digCount[10];
	cin >> T;
	FOR(t, 1, T) {
		cin >> S;
		memset(letter, 0, sizeof(letter));
		memset(digCount, 0, sizeof(digCount));
		REP(i, S.size()) {
			letter[S[i] - 'A']++;
		}
		digCount[0] = letter['Z'- 'A'];
		takeDigit(0, digCount[0]);

		digCount[2] = letter['W' - 'A'];
		takeDigit(2, digCount[2]);

		digCount[4] = letter['U' - 'A'];
		takeDigit(4, digCount[4]);

		digCount[6] = letter['X' - 'A'];
		takeDigit(6, digCount[6]);

		digCount[8] = letter['G' - 'A'];
		takeDigit(8, digCount[8]);

		digCount[1] = letter['O' - 'A'];
		takeDigit(1, digCount[1]);

		digCount[3] = letter['T' - 'A'];
		takeDigit(3, digCount[3]);

		digCount[5] = letter['F' - 'A'];
		takeDigit(5, digCount[5]);

		digCount[7] = letter['S' - 'A'];
		takeDigit(7, digCount[7]);

		digCount[9] = letter['I' - 'A'];
		takeDigit(9, digCount[9]);

		cout << "Case #" << t << ": ";
		REP(i, 10) {
			if (digCount[i] != 0) {
				REP(j, digCount[i]) {
					cout << i;
				}
			}
		}
		cout << endl;
	}

	return 0;
}
