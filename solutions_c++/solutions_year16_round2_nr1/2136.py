#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int ai(char c) { return c - 'A'; }

int main() {
	int numTests;
	scanf("%d\n", &numTests);
	for (int z = 0; z < numTests; ++z) {

		char str[2002];
		scanf("%s\n", str);
		int numChars = strlen(str);

		int numLetters[26];
		for (int i = 0; i < 26; ++i) {
			numLetters[i] = 0;
		}
		int foundLetters[10];
		for (int i = 0; i < 10; ++i) {
			foundLetters[i] = 0;
		}

		for (int i = 0; i < numChars; ++i) {
			numLetters[str[i] - 'A']++;
		}

		while (numLetters[ai('Z')] > 0) {
			numLetters[ai('Z')]--;
			numLetters[ai('E')]--;
			numLetters[ai('R')]--;
			numLetters[ai('O')]--;
			foundLetters[0]++;
		}
		while (numLetters[ai('W')] > 0) {
			numLetters[ai('T')]--;
			numLetters[ai('W')]--;
			numLetters[ai('O')]--;
			foundLetters[2]++;
		}
		while (numLetters[ai('G')] > 0) {
			numLetters[ai('E')]--;
			numLetters[ai('I')]--;
			numLetters[ai('G')]--;
			numLetters[ai('H')]--;
			numLetters[ai('T')]--;
			foundLetters[8]++;
		}
		while (numLetters[ai('X')] > 0) {
			numLetters[ai('S')]--;
			numLetters[ai('I')]--;
			numLetters[ai('X')]--;
			foundLetters[6]++;
		}
		while (numLetters[ai('S')] > 0) {
			numLetters[ai('S')]--;
			numLetters[ai('E')]--;
			numLetters[ai('V')]--;
			numLetters[ai('E')]--;
			numLetters[ai('N')]--;
			foundLetters[7]++;
		}
		while (numLetters[ai('H')] > 0) {
			numLetters[ai('T')]--;
			numLetters[ai('H')]--;
			numLetters[ai('R')]--;
			numLetters[ai('E')]--;
			numLetters[ai('E')]--;
			foundLetters[3]++;
		}
		while (numLetters[ai('R')] > 0) {
			numLetters[ai('F')]--;
			numLetters[ai('O')]--;
			numLetters[ai('U')]--;
			numLetters[ai('R')]--;
			foundLetters[4]++;
		}
		while (numLetters[ai('F')] > 0) {
			numLetters[ai('F')]--;
			numLetters[ai('I')]--;
			numLetters[ai('V')]--;
			numLetters[ai('E')]--;
			foundLetters[5]++;
		}
		while (numLetters[ai('O')] > 0) {
			numLetters[ai('O')]--;
			numLetters[ai('N')]--;
			numLetters[ai('E')]--;
			foundLetters[1]++;
		}
		while (numLetters[ai('I')] > 0) {
			numLetters[ai('N')]--;
			numLetters[ai('I')]--;
			numLetters[ai('N')]--;
			numLetters[ai('E')]--;
			foundLetters[9]++;
		}


		cout << "Case #" << (z + 1) << ": ";
		for (int i = 0; i < 10; ++i) {
			for (int k = 0; k < foundLetters[i]; ++k) {
				cout << i;
			}
		}
		cout << endl;
	}
}
/*0 = "Z" ZERO
2 = "W" TWO
8 = "G" EIGHT
6 = "X" SIX
7 = "S" SEVEN
3 = "H" THREE
4 = "R" FOUR
5 = "F" FIVE
1 = "O" ONE
9 = "I" NINE*/