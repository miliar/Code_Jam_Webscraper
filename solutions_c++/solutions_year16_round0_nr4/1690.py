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

void printB(int v, int d) {
	for (int i = d - 1; i >= 0; --i)
		cout << (((1 << i) & v) > 0 ? 1 : 0);
	cout << ' ';
}

int process(int v, int len, int step) {
	int res = v;
	int l = len;
	int b = (1 << len) - 1;
	for (int i = 1; i < step; ++res) {
		int nr = 0;
		for (int j = 0; j < len; ++j) {

		}
		res = nr;
	}
	return res;
}

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	/*
	for (int i = 1; i <= 100000; ++i)
		cout << i << ' ' << solve(i) << endl;
	return 0;
	int s = 3, k = 1;
	for (int i = 0; i < (1 << s); ++i) {
		printB(i, s);
		cout << endl;
	}*/
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";
		
		lli k, c, s;
		cin >> k >> c >> s;
		if (c == 1) {
			if (s < k) cout << "IMPOSSIBLE";
			else for (int i = 1; i <= k; ++i) cout << i << ' ';
		} 
		else {
			if (2 * s < k) cout << "IMPOSSIBLE";
			else {
				lli len = 1;
				for (int i = 1; i < c; ++i) len *= k;
				lli offset = 2;
				lli pos = 0;
				while (offset <= k) {
					cout << pos + offset << ' ';
					pos += 2*len;
					offset += 2;
				}
				if (k & 1) {
					cout << len * k;
				}
			}
		}

		cout << endl;
	}
}