#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int containsMinus(string s) {
	if (s.find_first_of("-") == string::npos)
		return false;
	return true;
}

string flip(string s, int num) {
	string subStr = s.substr(0,num);
	string newString = string(subStr.rbegin(), subStr.rend());
	std::replace(newString.begin(), newString.end(), '+', 't');
	std::replace(newString.begin(), newString.end(), '-', '+');
	std::replace(newString.begin(), newString.end(), 't', '-');
	if (num < s.length())
		newString += string(s.begin() + num, s.end());
	if (s == newString)
		newString = flip(s, num - 1);
	//cout << newString << '\n';
	return newString;
}

void lowestAmount(string s, size_t turn) {
	if (containsMinus(s) > 0) {
		bool started = false;
		size_t index = 0;
		char prevChar = 'x';
		for (auto it = s.begin(); it < s.end(); it++, ++index) {
			//cout << (*it != prevChar);
			if (*it != prevChar && started) {
				lowestAmount(flip(s, index), turn + 1);
				return;
			}
			else if (index + 1 == s.length()) {
				//cout << s << '\n';
				lowestAmount(flip(s, index + 1), turn + 1);
				return;
			}
			started = true;
			prevChar = *it;
		}

	} else {
		cout << to_string(turn) << '\n';
	}
}

int main(int argc, char *argv[])
{
	string line = "";
	getline(cin,line);
	int caseNum = 1;
	while (getline(cin, line)) {
		cout << "Case #" + to_string(caseNum++) + ": ";
		lowestAmount(line, 0);
	}
}