#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

bool isValid(string s, int n) {
	string t = "";
	int len = s.size();
	if (n >= pow(10, len)) {
		return false;
	}
	for (int i = 0; i < len; i++) {
		char c = s[len - i - 1];
		int  h = (int(n / pow(10, i))) % 10;
		if (c != '?' && (c - '0') != h) {
			return false;
		}
	}
	//cout << s << " : " << n << endl;
	return true;
}
string padZero(string s, int n) {
	int len = s.size();
	int count = 0;
	string ret = "";
	while (n > 0) {
		ret = char('0' + (n % 10)) + ret;
		n /= 10;
		count++;
	}
	for (int i = 0; i < len - count; i++) {
		ret = '0' + ret;
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string c, d;
		cin >> c >> d;

		/* solution */
		int mxDiff = 10000;
		int minC = 0;
		int minD = 0;
		for (int i = 0; i < 1000; i++) {
			if (isValid(c, i)) {
				for (int j = 0; j < 1000; j++) {
					if (isValid(d, j)) {
						if (abs(i - j) < mxDiff) {
							mxDiff = abs(i - j);
							minC = i;
							minD = j;
						}
					}
				}
			}
		}
		cout << "Case #" << t << ": " << padZero(c, minC) << " " << padZero(d, minD) << endl;
	}
}

