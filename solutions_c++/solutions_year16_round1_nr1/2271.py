#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 1e6;
#define MP make_pair
#define lli long long int

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	/*
	for (int n = 0; n < 100; ++n) {
		string s = "";
		for (int i = 0; i < 1000; ++i) {
			if (rand() & 1) s = 'a' + s;
			else s = s + 'a';
		}
		cout << s;
	}*/

	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";
		
		string s;
		cin >> s;
		string ans = "";
		for (int i = 0; i < s.length(); ++i) {
			if (!i || ans[0] <= s[i]) ans = s[i] + ans;
			else ans += s[i];
		}
		cout << ans;

		cout << endl;
	}
}