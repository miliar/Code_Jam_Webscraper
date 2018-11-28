#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <vector>

using namespace std;

int pancakes(string stack);

int main() {
	int num_test_cases;
	string line;
	getline(cin, line);
	istringstream convert(line);
	convert >> num_test_cases;
	//cout << "Num cases: " << num_test_cases << endl;
	for (int i = 0; i < num_test_cases; i++) {
		getline(cin, line);
		int min_moves = pancakes(line);
		cout << "Case #" << i+1 << ": " << min_moves << endl;
	}
	return 0;
}

void print_pancake(vector<bool> &stack) {
	// Print pancake
	for (bool b : stack) {
		if (b == 0) {
			cout << "-";
		} else {
			cout << "+";
		}
	}
	cout << endl;
	return;
}

void flip(vector<bool> &stack, int position) {
	// Exchange elements
	for (int i = 0; i < position / 2 + 1; i++) {
		bool temp = stack[i];
		stack[i] = stack[position - i];
		stack[position - i] = temp;
	}

	// Reverse signs
	for (int i =0; i <= position; i++) {
		stack[i] = !stack[i];
	}

	//cout << "flip " << position << endl;
}

bool sorted(const vector<bool> &stack) {
	for (bool b : stack) {
		if (b == 0) { return false; }
	}
	return true;
}

int pancakes(string stack) {
	// Pancake stack 0 = down; 1 = up
	vector<bool> pstack(stack.size());

	// Parse pancake
	for (unsigned i = 0; i < stack.size(); i++) {
		//cout << stack[i];
		if (stack[i] == '+') {
			pstack[i] = 1;
		} else {
			pstack[i] = 0;
		}
	}
	//cout << endl;

	int min_flips = 0;
	while(!sorted(pstack)) {
		bool ref = pstack[0];
		int flp_indx = 0;
		for (unsigned i = 0; i < pstack.size(); i++) {
			if (pstack[i] != ref) { break; }
			flp_indx = i;
		}
		flip(pstack, flp_indx);
		min_flips++;
		//print_pancake(pstack);
	}
	//print_pancake(pstack);
	return min_flips;
}

