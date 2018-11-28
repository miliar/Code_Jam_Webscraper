// CodeJamPractice.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

static string strTbl[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

bool checkAndMinus(const string &curStr, vector<int> &cnt) {
	for (int i = 0; i < curStr.length(); ++i) {
		if (cnt[curStr[i] - 'A'] == 0) {
			return false;
		}
	}
	for (int i = 0; i < curStr.length(); ++i) {
		--cnt[curStr[i] - 'A'];
	}
	return true;
}

inline void add(vector<int> &cnt, const string &curStr) {
	for (int i = 0; i < curStr.length(); ++i) {
		++cnt[curStr[i] - 'A'];
	}
}

bool valid(vector<int> &cnt) {
	for (int i = 0; i < cnt.size(); ++i) {
		if (cnt[i] != 0) {
			return false;
		}
	}
	return true;
}

bool dfs(vector<int> &cnt, string &res) {
	string curStr = "";
	for (int i = 0; i <= 9; ++i) {
		curStr = strTbl[i];
		if (checkAndMinus(curStr, cnt)) {
			res += (i+'0');
			if (dfs(cnt, res)) {
				return true;
			}
			else {
				add(cnt, curStr);
				res = res.substr(0, res.length()-1);
			}
		}
	}
	if (valid(cnt)) {
		return true;
	}
	else {
		return false;
	}
}

int main()
{
	ifstream in("A-small-attempt0.in");
	streambuf *cinbuf = cin.rdbuf();
	cin.rdbuf(in.rdbuf());

	ofstream out("A-small-attempt0.out");
	streambuf *coutbuf = cout.rdbuf();
	cout.rdbuf(out.rdbuf());


	int t;
	string str;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> str;
		vector<int> cnt(26, 0);
		for (int j = 0; j < str.length(); ++j) {
			cnt[str[j] - 'A']++;
		}

		string res = "";
		dfs(cnt, res);
		cout << "Case #" << i << ": " << res << endl;
	}
	system("pause");
    return 0;
}

