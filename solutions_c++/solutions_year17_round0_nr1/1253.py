#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <stdio.h>
#include <string.h>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

char flip(char a) {
	if (a == '-')
		return '+';
	return '-';
}

void main() {
	int t;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		char pancakes[1001];
		int n = 0;
		cin >> pancakes >> n;
		char previous = '+';

		int totalLen = strlen(pancakes), countStep = 0;
		for (int j = totalLen - 1; j >= n - 1; j--) {
			if (pancakes[j] != '+') {
				countStep++;
				for (int k = 0; k < n; k++) {
					pancakes[j - k] = flip(pancakes[j - k]);
				}

			}
		}
		bool gotAnswer = true;
		for (int j = totalLen - 1; j >= 0; j--) {
			if (pancakes[j] == '-') {
				gotAnswer = false;
				j = -1;
			}
		}
		if(gotAnswer)
			cout << "Case #" << i << ": " << countStep << endl;
		else
			cout << "Case #" << i << ": IMPOSSIBLE " << endl;
	}
}