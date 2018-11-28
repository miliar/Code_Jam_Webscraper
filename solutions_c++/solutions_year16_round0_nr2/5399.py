#include <cmath>
#include <fstream>
#include <iostream>

using namespace std;

unsigned long T = 0;

int countFlips(string stack) {
	int count = 0;
	int lastInd = 0;

	for (int i = stack.size() - 1; i >= 0; i--) {
		if (stack[i] == '-') {
			lastInd = i + 1;
			break;
		}
	}
	string substack = string(stack.begin(), stack.begin() + lastInd);
	if (substack == "") {
		return 0;
	}
	lastInd = 0;
	while (substack[substack.size()-1] == '-') {
		if (substack[0] == '+') {
			for (int i = 0; i < substack.size(); i++) {
				if (substack[i] == '-') {
					break;
				} else {
					substack[i] = '-';
				}
			}
		} else {
			for (int i = 0; i < substack.size(); i++) {
				if (substack[i] == '+') {
					break;
				} else {
					substack[i] = '+';
				}
			}
		}
		count++;
	}

	return count;
}

int main(int argc, char **argv) {
	string stack;
	fstream fin(argv[1]);
	fin >> T;
	for (unsigned long i = 0; i < T; i++) {
		fin >> stack;
		int count = countFlips(stack);
		cout << "Case #" << i + 1 << ": " << count << endl;
	}

	return 0;
}
