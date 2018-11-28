#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

void extract(int charCount[], const char word[]) {
	for (const char* c = word; *c; c++) {
		charCount[*c]--;
	}
}

string solve(const string& s) {
	int sol[10];
	memset(sol, 0, sizeof(sol));

	int charCount[256];
	memset(charCount, 0, sizeof(charCount));

	for (int i = 0; i < s.length(); i++) {
		charCount[ s[i] ]++;
	}

	while (charCount['Z']) {
		extract(charCount, "ZERO");
		sol[0]++;
	}

	while (charCount['W']) {
		extract(charCount, "TWO");
		sol[2]++;
	}

	while (charCount['U']) {
		extract(charCount, "FOUR");
		sol[4]++;
	}

	while (charCount['X']) {
		extract(charCount, "SIX");
		sol[6]++;
	}

	while (charCount['G']) {
		extract(charCount, "EIGHT");
		sol[8]++;
	}

	while (charCount['O']) {
		extract(charCount, "ONE");
		sol[1]++;
	}

	while (charCount['H']) {
		extract(charCount, "THREE");
		sol[3]++;
	}

	while (charCount['F']) {
		extract(charCount, "FIVE");
		sol[5]++;
	}

	while (charCount['S']) {
		extract(charCount, "SEVEN");
		sol[7]++;
	}

	while (charCount['I']) {
		extract(charCount, "NINE");
		sol[9]++;
	}

	string r;
	for (int i = 0; i < 10; i++) {
		//cout << "sol[" << i << "] = " << sol[i] << endl;
		while (sol[i]--) {
			r = r + (char)('0' + i);
		}
	}
	return r;
}

int main() {
	string s;
	int tcases;
	cin >> tcases;
	for (int t = 1; t <= tcases; t++) {
		cin >> s;
		cout << "Case #" << t << ": " << solve(s) << endl;
	}
	return 0;
}
