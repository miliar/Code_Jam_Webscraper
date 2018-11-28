#include <iostream>
#include <sstream>
#include <string>

using namespace std;

string flip(string stack, size_t pos) {
	string s;
	for (size_t i = 0; i <= pos; ++i) {
		s += (stack[pos -i] == '-') ? '+' : '-';
	}
	for (size_t i = pos+1; i < stack.size(); ++i) {
		s += stack[i];
	}
	return s;
}

size_t process(string stack) {
	size_t count = 0;
	size_t posMinus, posPlus;
	while ((posMinus = stack.rfind('-')) != string::npos) {
		++count;
		posPlus = stack.find('+');
		if (posPlus == string::npos || posPlus > posMinus) {
			// last batch to flip
			return count;
		}
		// ...+- flip as many leading - as possible
		if (stack[0] == '-') {
			stack = flip(stack, posMinus);
		} else {
			// flip leading + first
			posMinus = stack.find('-');
			stack = flip(stack, posMinus-1);
		}
	}
	return count;
}

int main(int argc, char** argv) {
	size_t inputCount;
	cin >> inputCount;
	for (size_t inputNumber = 1; inputNumber <= inputCount; ++inputNumber) {
		string stack;
		cin >> stack;
		cout << "Case #" << inputNumber << ": ";
		cout << process(stack);
		cout << endl;
	}
	return 0;
}
