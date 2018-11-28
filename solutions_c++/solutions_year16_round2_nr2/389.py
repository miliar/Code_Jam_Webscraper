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
#define y1 y123123

unsigned lli minDiff = (1ull << 63ull);
int n;
char s1[20], s2[20];
string ans1, ans2;

void clear() {
	minDiff = (1ull << 63ull);
	memset(s1, 0, 20 * sizeof(char));
	memset(s2, 0, 20 * sizeof(char));
}

void solve(lli curDif, int pos, int b) {
	if (pos == n) {
		lli dif = 0;
		for (int i = 0; i < n; ++i) {
			dif = 10 * dif + ((int)s1[i] - (int)s2[i]);
		}
		if (dif < 0) dif = -dif;
		if (dif < minDiff) {
			ans1 = string(s1);
			ans2 = string(s2);
			minDiff = dif;
		}
		return;
	}
	char c1 = s1[pos], c2 = s2[pos];

	if (c1 != '?' && c2 != '?') {
		if (b == 0) {
			solve(curDif, pos + 1, (c1 < c2 ? -1 : (c1 == c2 ? 0 : 1)));
		}
		else {
			solve(curDif, pos + 1, b);
		}
	} else if (b == 0) {
		if (c1 == c2 && c1 == '?') {
			s1[pos] = s2[pos] = '0';
			solve(curDif, pos + 1, b);

			s1[pos] = '0';
			s2[pos] = '1';
			solve(curDif, pos + 1, -1);

			s2[pos] = '0';
			s1[pos] = '1';
			solve(curDif, pos + 1, 1);
		} else if (c1 == '?') {
			
			if (s2[pos] > '0') {
				s1[pos] = s2[pos] - 1;
				solve(curDif, pos + 1, -1);
			}
			s1[pos] = s2[pos];
			solve(curDif, pos + 1, 0);
			if (s2[pos] < '9') {
				s1[pos] = s2[pos] + 1;
				solve(curDif, pos + 1, 1);
			}			
		}
		else {			
			if (s1[pos] > '0') {
				s2[pos] = s1[pos] - 1;
				solve(curDif, pos + 1, 1);
			}
			s2[pos] = s1[pos];
			solve(curDif, pos + 1, 0);
			if (s1[pos] < '9') {
				s2[pos] = s1[pos] + 1;
				solve(curDif, pos + 1, -1);
			}			
		}
	} else if (b == -1) {
		s1[pos] = (s1[pos] == '?' ? '9' : s1[pos]);
		s2[pos] = (s2[pos] == '?' ? '0' : s2[pos]);
		solve(curDif, pos + 1, b);
	} else {
		s1[pos] = (s1[pos] == '?' ? '0' : s1[pos]);
		s2[pos] = (s2[pos] == '?' ? '9' : s2[pos]);
		solve(curDif, pos + 1, b);
	}

	s1[pos] = c1; s2[pos] = c2;
}

int pp[20] = { 1, 10, 100, 1000, 10000 };

pair<int, int> stupid() {
	int diff = 10000000;
	int bound = pp[n];
	pair<int, int> ans = MP(0, 0);
	for (int i = 0; i < bound; ++i) {
		bool ok = 1;
		for (int k = 0; k < n; ++k) {
			if (s1[n-k-1] == '?' || s1[n-k-1] - '0' == ((i / pp[k]) % 10)) {}
			else ok = false;
		}
		if (!ok) continue;
		for (int j = 0; j < bound; ++j) {
			ok = 1;
			for (int k = 0; k < n; ++k) {
				if (s2[n-k-1] == '?' || s2[n-k-1] - '0' == ((j / pp[k]) % 10)) {}
				else ok = false;
			}
			if (!ok) continue;
			int d = max(i - j, j - i);
			if (d < diff || (d == diff && i < ans.first) || (d == diff && i == ans.first && j < ans.second)) {
				diff = d;
				ans = MP(i, j);
			}
		}
	}
	return ans;
}

void pr(int v) {
	int k = n - 1;
	while (k > 0 && pp[k] > v) {
		cout << 0; --k;
	}
	cout << v;
}

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		scanf("%s %s", &s1, &s2);
		n = strlen(s1);
		solve(0, 0, 0);
		cout << ans1 << ' ' << ans2;
		//pair<int, int> a = stupid();
		//cout << a.first << ' ' << a.second;
		//pr(a.first); cout << ' '; pr(a.second);
		clear();

		cout << endl;
	}
}
