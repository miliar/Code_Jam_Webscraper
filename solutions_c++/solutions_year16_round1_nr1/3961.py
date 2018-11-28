#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#define SUBMIT 1
using namespace std;


string solve(const string &s, const char i, bool firstappear) {
	if (s == "" || i < 'A') return "";
	vector<string> vs;
	string ret="", tobesolved="";
	int prv = 0, sublen = 0, wordcnt=0;
	for (int j = 0; j < s.length(); j++) {
		if (s[j] == i) {
			if (wordcnt == 0 && !firstappear) {
				tobesolved = s.substr(prv, sublen);
			}
			else {
				vs.push_back(s.substr(prv, sublen));
			}
			wordcnt++;
			sublen = 0;
			prv = j + 1;
			firstappear = true;
		}
		else {
			sublen++;
		}
	}
	if (wordcnt == 0 && !firstappear) {
		tobesolved = s.substr(prv, sublen);
	}
	else {
		vs.push_back(s.substr(prv, sublen));
	}
	
	while (wordcnt--) ret += "" + string(1, char(i));
	
	ret += solve(tobesolved, i - 1, false);
	for (const string& str : vs) {
		ret += str;
	}

	return ret;
}

int main(void) {
	if (SUBMIT) {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}

	int T; scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		


		string s; cin >> s;
		printf("Case #%d: ", tc);
		cout <<  solve(s, 'Z', false) << endl;
	}
}