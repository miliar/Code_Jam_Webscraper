#include <iostream>
#include <string>

using namespace std;

char change(char c) {
	if (c == '+') {
		return '-';
	}
	if (c == '-') {
		return '+';
	}
	return '*';
}

void flip(string *s, int top, int bottom) {
	string temp = "";
	for (int i = top; i <= bottom; i++) {
		temp += (*s).at(i);
	}
	for (int i = top, j = temp.length() - 1; i <= bottom; i++, j--) {
		(*s).at(i) = change(temp.at(j));
	}
}

__int64 eval(string *s, int top, int bottom, char c) {
	if ((top == 0) && (bottom == 0) && ((*s).at(0) == c)) {
		return 0;
	}
	if ((top == 0) && (bottom == 0) && ((*s).at(0) != c)) {
		(*s).at(0) = change((*s).at(0));
		return 1;
	}
	if ((*s).at(bottom) == c) {
		return eval(s, top, bottom - 1, c);
	}
	else {
		if ((*s).at(top) != (*s).at(bottom)) {
			int t = 0;
			while ((t + 1 < (*s).length()) && ((*s).at(t + 1) == (*s).at(t))) {
				t++;
			}
			flip(s, top, t);
			flip(s, top, bottom);
			return eval(s, top, bottom, c) + 2;
		}
		else {
			

			flip(s, top, bottom);
			return eval(s, top, bottom, c) + 1;
		}
	}
}

int main() {
	int testCases;
	__int64 number = 0;
	string s;
	int top;
	int bottom;
	cin >> testCases;
	for (int testCase = 1; testCase <= testCases; testCase++) {
		cin >> s;
		top = 0;
		bottom = s.length() - 1;
		number = eval(&s, top, bottom, '+');
		printf("Case #%d: %llu\n", testCase, number);
	}
}