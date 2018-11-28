#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>
#include <memory.h>
#include <sstream>
#include <array>

using namespace std;

char win(char a, char b) {
	if (a > b) {
		swap(a, b);
	}
	if (a == 'P') {
		if (b == 'S') {
			return 'S';
		} else {
			return 'P';
		}
	}
	else if (a == 'R') {
		return 'R';
	}
}


int main() {
	//ios_base::sync_with_stdio(false);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		string ans = "";
		string cur = "";
		for (int i = 0; i < r; i++) {
			cur += "R";
		}
		for (int i = 0; i < p; i++) {
			cur += "P";
		}
		for (int i = 0; i < s; i++) {
			cur += "S";
		}

		sort(cur.begin(), cur.end());
		do {
			string str = cur;
			bool ok = true;
			while (str.length() > 1 && ok) {
				string left = "";
				for (int i = 0; i < str.length() && ok; i += 2) {
					if (str[i] == str[i + 1]) {
						ok = false;
						break;
					}
					left += win(str[i], str[i + 1]);
				}
				str = left;
			}
			if (ok) {
				if (ans == "" || cur < ans) {
					ans = cur;
				}
			}
		} while (next_permutation(cur.begin(), cur.end()));

		cout << "Case #" << test << ": ";
		if (ans == "") {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << ans;
		}
		cout << endl;

	}


	//system("pause");
	return 0;
}