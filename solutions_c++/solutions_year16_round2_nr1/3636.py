#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;


char KEYMAP[10][10] = {
	"ZERO",
	"ONE",
	"TWO",
	"THREE",
	"FOUR",
	"FIVE",
	"SIX",
	"SEVEN",
	"EIGHT",
	"NINE"
};


bool checking(int number, vector<int> status) {
	string str = KEYMAP[number];
	bool valid = true;
	for (unsigned int i=0; valid && i<str.size(); i++) {
		valid &= (status[str[i]] > 0);
		status[str[i]]--;
	}
	return valid;
}

vector<int> reduce(int number, vector<int> status) {
	string str = KEYMAP[number];
	for (unsigned int i=0; i<str.size(); i++) {
		status[str[i]]--;
	}
	return status;
}
typedef pair<bool, string> RESULT;

bool statusEmpty(const vector<int>& status) {
	bool valid = true;
	for (int i='A'; true && i<='Z'; i++) {
		valid &= (status[i] == 0);
	}
	return valid;
}

RESULT action(int number, vector<int> status, string ans) {
	if (statusEmpty(status)) {
		return make_pair(true, ans);
	}
	if (number > 9) {
		return make_pair(false, ans);
	}
	if (checking(number, status)) {
		RESULT act = action(number, reduce(number, status), ans + (char)('0' + number));
		if (act.first) {
			return act;
		}
	}
	return action(number + 1, status, ans);
}

void execute(int tc) {
	string input;
	cin >> input;
	vector<int> counter('Z'+1, 0);
	for (unsigned int i=0; i< input.size(); i++) {
		counter[input[i]]++;
	}
	RESULT ans = action(0, counter, "");
	printf("Case #%d: %s\n", tc, ans.second.c_str());
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i=1; i<=T; i++) {
		execute(i);
	}
	return 0;
}
