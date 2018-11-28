#include <iostream>
using namespace std;

int checkTestCase(string s);

int main() {
	int testCases = 0;
	cin >> testCases;
	string testCasesArr[testCases];
	for(int i = 0; i < testCases; i++) {
		cin >> testCasesArr[i];
	}
	for(int i = 0; i < testCases; i++) {
		int result = checkTestCase(testCasesArr[i]);
			cout << "Case #" << i + 1 << ": " << result << endl;
	}
	return 0;
}

int checkTestCase(string s) {
	int count = 0;
	int size = s.size();
	s.push_back('+');
	for(int i = 0; i < size; i++) {
		if(s[i] == '-' && s[i+1] == '+') {
			count++;
		} else if(s[i] == '-' && s[i+1] == '-') {
			//Do nothing?
		} else if(s[i] == '+' && s[i+1] == '-') {
			count++;
		} else {
			//do nothing?
		}
	}
	return count;
}
