#include <iostream>
#include <string>

#define MAX_T   (100)
#define MAX_S   (100)

using namespace std;

int find(const string &s, char c, bool first) {
	if(first) {
		for(int i = 0; i < s.size(); ++i)
			if(s[i] == c)
				return i;
	} else {
		for(int i = (int)s.size() - 1; i >= 0; --i)
			if(s[i] == c)
				return i;
	}
	return -1;
}

void flip(string &s, int bottom) {
	for(int i = 0, j = bottom; i < j; ++i, --j) {
		swap(s[i], s[j]);
		s[i] = (s[i] == '+')? '-': '+';
		s[j] = (s[j] == '+')? '-': '+';
	}

	if((bottom % 2) == 0)
		s[bottom/2] = (s[bottom/2] == '+')? '-': '+';
}

bool complete(const string &s) {
	for(char c : s)
		if(c == '-')
			return false;
	return true;
}

int solve(string &s) {
	if(complete(s))
		return 0;

	int idx;
	if(s[0] == '-') {
		idx = find(s, '-', false);
		flip(s, idx);
	} else {
		idx = find(s, '-', true);
		flip(s, idx - 1);
	}

	return 1 + solve(s);
}

int main(void) {
	cout.sync_with_stdio(false);

	int nTests;
	cin >> nTests;

	for(int t = 1; t <= nTests; ++t) {
		string s;
		cin >> s;
		cout << "Case #" << t << ": ";
		cout << solve(s) << endl;
	}

	return 0;
}
