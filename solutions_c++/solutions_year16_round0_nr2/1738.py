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
	/*
	for (int i = 1; i <= 100000; ++i)
		cout << i << ' ' << solve(i) << endl;
	return 0;*/
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << qq + 1 << ": ";
		string s;
		cin >> s;
		char last = s[0];
		int ans = 0;
		for (int i = 1; i < s.length(); ++i) {
			if (s[i] != last) {
				last = s[i];
				++ans;
			}
		}
		if (last == '-') ++ans;
		cout << ans;
		cout << endl;
	}
}