#include <iostream>
#include <string>

using namespace std;

size_t findLast(const std::string & s) {
	size_t pos = s.size();
	size_t result = pos;
	char last = 'A' - 1;
	while (pos > 0) {
		--pos;
		if (s[pos] > last) {
			last = s[pos];
			result = pos;
		}
	}
	return result;
}

void process(string S) {
	// find last letter from left to right, then complete the word from left to right
	string s = S;
	string result;
	string remain;
	while (!s.empty()) {
		size_t pos = findLast(s);
		result += s[pos];
		if (pos < s.size()-1) {
			remain = s.substr(pos+1) + remain;
		}
		if (pos) {
			s = s.substr(0, pos);
		} else {
			s.clear();
		}
	}
	result.append(remain);
	cout << result << endl;
}

int main(int argc, char** argv) {
	size_t inputCount;
	cin >> inputCount;
	for (size_t inputNumber = 1; inputNumber <= inputCount; ++inputNumber) {
		string s;
		cin >> s;
		cout << "Case #" << inputNumber << ": ";
		process(s);
	}
	return 0;
}
