#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int flip(vector<int>& vstack) {
	while (!vstack.empty()) {
		if (vstack.back() == 1)
			vstack.pop_back();
		else
			break;
	}
	if (vstack.empty()) return 0;
	// Flip all the + pancakes on top
	if (vstack[0] == 1) {
		int i = 0;
		while (vstack[i] == 1) {
			vstack[i++] = -1;
		}
	}
	// Flip all the pancakes if they begin and end by a -
	else {
		reverse(vstack.begin(), vstack.end());
		for (int i = 0; i < vstack.size(); ++i) {
			vstack[i] *= -1;
		}
	}
	return 1 + flip(vstack);
}

int maxFlips(string stack) {
	vector<int> vstack;
	for (int i = 0; i < stack.size(); ++i) {
		vstack.push_back(((stack[i] == '+') ? 1 : -1));
	}
	return flip(vstack);
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	string stack;
	for (int c = 0; c < T; ++c) {
		cin >> stack;
		cout << "Case #" << c + 1 << ": " << maxFlips(stack) << endl;
	}
	return 0;
}