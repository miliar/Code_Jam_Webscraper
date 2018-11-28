#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;

string resStr1, resStr2;
int cmpCom;

bool isTrue(string &str1, string &str2, int k) {
	for (int i = k; i < str1.size(); i++) {
		if (str1[i] == '?' || str2[i] == '?')
			return true;
	}
	return false;
}
int isMore(string &str1, string &str2, int k) {
	for (int i = 0; i < str1.size(); i++) {
		if (str1[i] != '?' && str2[i] != '?') {
			if (str1[i] < str2[i]) {
				return 1;
			}
			else if (str1[i] > str2[i])
				return -1;
		}
	}

	return 0;
}
void backtrack(string &str1, string &str2, int k) {
	if (k == str1.size()) {
		if (resStr1 == "") {
			resStr1 = str1;
			resStr2 = str2;
		}
		else {
			int A = abs(atoi(resStr1.c_str()) - atoi(resStr2.c_str()));
			int B = abs(atoi(str1.c_str()) - atoi(str2.c_str()));

			if (A > B) {
				resStr1 = str1;
				resStr2 = str2;
			}
		}
		return;
	}

	if (str1[k] == '?' && str2[k] == '?') {
			str1[k] = '0';
			str2[k] = '0';
			backtrack(str1, str2, k + 1);
			str1[k] = '0';
			str2[k] = '1';
			backtrack(str1, str2, k + 1);
			str1[k] = '0';
			str2[k] = '9';
			backtrack(str1, str2, k + 1);
			str1[k] = '1';
			str2[k] = '0';
			backtrack(str1, str2, k + 1);
			str1[k] = '9';
			str2[k] = '0';
			backtrack(str1, str2, k + 1);

			str1[k] = '?';
			str2[k] = '?';
	}
	else if (str1[k] == '?') {
		str1[k] = '0';
		backtrack(str1, str2, k + 1);
		if (str2[k] != '0') {
			str1[k] = str2[k] - 1;
			backtrack(str1, str2, k + 1);
		}
		str1[k] = str2[k];
		backtrack(str1, str2, k + 1);
		if (str2[k] != '9') {
			str1[k] = str2[k] + 1;
			backtrack(str1, str2, k + 1);
		}
		str1[k] = '9';
		backtrack(str1, str2, k + 1);
		str1[k] = '?';
	}
	else if (str2[k] == '?') {
		str2[k] = '0';
		backtrack(str1, str2, k + 1);
		if (str1[k] != '0') {
			str2[k] = str1[k] - 1;
			backtrack(str1, str2, k + 1);
		}
		str2[k] = str1[k];
		backtrack(str1, str2, k + 1);
		if (str1[k] != '9') {
			str2[k] = str1[k] + 1;
			backtrack(str1, str2, k + 1);
		}
		str2[k] = '9';
		backtrack(str1, str2, k + 1);

		str2[k] = '?';
	}
	else {
		backtrack(str1, str2, k + 1);
	}
}

int main() {
	freopen("B8.in", "r", stdin);
	freopen("B8.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int TestCase = 1; TestCase <= T; TestCase++) {
		string str1, str2;
		resStr1 = resStr2 = "";
		cin >> str1 >> str2;
		cmpCom = -1;

		backtrack(str1, str2, 0);

		printf("Case #%d: ", TestCase);
		cout << resStr1 << " " << resStr2 << endl;
	}


	return 0;
}