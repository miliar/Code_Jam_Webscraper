#include <iostream>
#include <string>
#include <fstream>
#include <iterator>
#include <algorithm>
#include <stack>
#include <vector>
using namespace std;

int flippingPancakes(stack<char>& pancakes) {
	if (pancakes.size() == 0) { return 0; }
	if (pancakes.size() == 1) {
		if (pancakes.top() == '+') { return 0; }
		else { return 1; }
	}
	stack<char> aTray;
	int count = 0;
	while (pancakes.size() != 0) {
		aTray.push(pancakes.top());
		pancakes.pop();
		while (pancakes.size() != 0 && aTray.top() == pancakes.top()) {
			aTray.push(pancakes.top());
			pancakes.pop();
		}
		if (pancakes.size() == 0) {
			break;
		}
		else {
			if (aTray.top() == '-') {
				while (aTray.size() != 0) {
					pancakes.push('+');
					aTray.pop();
				}
				count = count + 1;
			}
			else {
				while (aTray.size() != 0) {
					pancakes.push('-');
					aTray.pop();
				}
				count = count + 1;
			}
		}
	}
	if (aTray.top() == '-') { count = count + 1; }
	return count;
}

int main() {
	size_t cases;
	ifstream ifs("Text.txt");
	if (!ifs) {
		cout << "can't open the file" << endl;
		exit(1);
	}
	ifs >> cases;
	for (size_t i = 1; i <= cases; i++) {
		stack<char> stackOfPancakes;
		string pancakes;
		ifs >> pancakes;
		for (string::iterator iter = pancakes.end()-1; iter > pancakes.begin(); --iter) {
			stackOfPancakes.push(*iter);
		}
		stackOfPancakes.push(*pancakes.begin());
		cout << "Case #" << i << ": " << flippingPancakes(stackOfPancakes) << endl;
	}
}