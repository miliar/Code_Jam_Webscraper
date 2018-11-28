#include <iostream>
#include <string>

using namespace std;

const char HAPPY = '+';
const char BLANK = '-';

char stack[101];

inline char flipOne(char c) {
	return c == HAPPY ? BLANK : HAPPY;
}

bool valid(int ssize) {
	for (int i = 0; i < ssize; i++) {
		if (stack[i] != HAPPY) return false;
	}
	return true;
}

void flip(int ssize) {
	// checks if the very top is blank, if so, start counting from top
	if (stack[0] != HAPPY) {
		int i = 0;
		while (stack[i] != HAPPY && i < ssize) {
			stack[i] = HAPPY;
			i++;
		}
		return;
	} else {
		// otherwise, flip the happies from the front
		int i = 0;
		while (stack[i] == HAPPY && i < ssize) {
			stack[i] = BLANK;
			i++;
		}
		return;
	}
}

int main(int argc, char** argv) {
	int cases;
	cin >> cases;

	for (int c = 1; c <= cases; c++) {
		string line;
		cin >> line;
		int ssize = line.size();
		for (int i = 0; i < ssize; i++) {
			stack[i] = line[i];
		}
		int flips = 0;
		while (!valid(ssize)) {
			flip(ssize);
			flips++;
		}
		cout << "Case #" << c << ": " << flips << endl;
	}

	return 0;
}
