#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isUp(char c) {
	return c == '+';
}

bool isDown(char c) {
	return c == '-';
}

int getFirstDown(string &stack) {
	for (int i = 0; i < stack.length(); ++i) {
		if (isDown(stack[i])) return i;
	}
	return -1;
}

void flipStack(string &stack, int firstDown) {
	if (firstDown == 0) {
		for (int i = 0; i < stack.length(); ++i) {
			if (isDown(stack[i])) stack[i] = '+';
			else return;
		}
	} else {
		for (int i = 0; i < stack.length(); ++i) {
			if (isUp(stack[i])) stack[i] = '-';
			else return;
		}
	}
}

int minNumOfFlips(string &stack) {
	int numFlips = 0;
	int firstDown = getFirstDown(stack);
	while (firstDown != -1) {
		flipStack(stack, firstDown);
		++numFlips;
		firstDown = getFirstDown(stack);
	}
	return numFlips;
}

int main( int argc, char** argv ) {
	int count = 0;
	cin >> count;
	for (int i = 0; i < count; ++i) {
		string stack;
		cin >> stack;
		// cout << minNumOfFlips(stack) << endl;
		cout << "Case #" << i + 1 << ": " << minNumOfFlips(stack) << endl;
		// cout << countingSheep(N) << endl;
	}
	return 0;
}
