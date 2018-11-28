#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<unistd.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include "../../ttmath/ttmath.h"

using namespace std;
string letters[] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

bool can_i(int *digits, int x) {
	int i = 0;
	for (; i < letters[x].size(); ++i)
		if (digits[letters[x].at(i) - 'A'] <= 0)
			return false;
	return true;
}

void add_word(int *digits, int x) {
	int i = 0;
	for (; i < letters[x].size(); ++i)
		digits[letters[x].at(i) - 'A']++;
}

void sub_word(int *digits, int x) {
	int i = 0;
	for (; i < letters[x].size(); ++i)
		digits[letters[x].at(i) - 'A']--;
}

string test(int *digits, int n, int x) {
	int i, j;
	bool used = true;
	for (j = 0; j < 26; ++j) {
		if (digits[j] > 0) {
			used = false;
			break;
		}
	}
	if (used)
		return "OK";
	if (n <= 0)
		return "";
	for (i = x; i < 10; ++i) {
		if (can_i(digits, i)) {
			sub_word(digits, i);
			string ret = test(digits, n-1, i);
			if (ret == "OK")
				return to_string(i);
			if (ret != "")
				return to_string(i) + ret;
			add_word(digits, i);
		}
	}
	return "";
}

/*
string test(int *digits, int n, int x) {
	cout << n << '\t' << x << endl;
	int i, j;
	bool used = true;
	for (j = 0; j < 26; ++j)
		if (digits[j]) {
			used = false;
			break;
		}
	if (used)
		return "OK";
	if (n <= 0)
		return "";
	for (i = x; i < 10; ++i)
	{
		bool ok = true;
		for (j = 0; j < letters[i].size(); ++j)
			if (digits[letters[i].at(j)-'A'] == 0) {
				cout << letters[i];
				ok = false;
				break;
			}
		if (!ok)
			continue;
		for (j = 0; j < letters[i].size(); ++j)
			--digits[letters[i].at(j)-'A'];
		cout << endl;
		string ret = test(digits, n-1, i);
		if (ret == "OK")
			return to_string(i);
		else {
			for (j = 0; j < letters[i].size(); ++j)
				++digits[letters[i].at(j)-'A'];
		}
	}
	return "";
}
*/
int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	unsigned int n, N, t, tm, i, j;
	string s;
	cin >> N;
	int digits[26];
	for (i = 0; i < N; ++i) {
		printf("Case #%d: ", i+1);
		cin >> s;
		memset(digits, 0, sizeof(digits));
		for (j = 0; j < s.size(); ++j)
			++digits[s.at(j) - 'A'];
		cout << test(digits, 10, 0) << endl;
	}
	return 0;
}
