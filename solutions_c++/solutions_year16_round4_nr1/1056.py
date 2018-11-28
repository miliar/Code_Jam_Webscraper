#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>

using namespace std;

void can(int n, int &r, int &p, int &s, char p1, char p2) {
	if (p2 == 'R')
		r++;
	if (p2 == 'P')
		p++;
	if (p2 == 'S')
		s++;
	if (n == 1)
		return;
	if (p1 == 'R') {
		can(n - 1, r, p, s, p1, 'S');
	}
	if (p1 == 'P') {
		can(n - 1, r, p, s, p1, 'R');
	}
	if (p1 == 'S') {
		can(n - 1, r, p, s, p1, 'P');
	}
	if (p2 == 'R') {
		can(n - 1, r, p, s, p2, 'S');
	}
	if (p2 == 'P') {
		can(n - 1, r, p, s, p2, 'R');
	}
	if (p2 == 'S') {
		can(n - 1, r, p, s, p2, 'P');
	}
}

string ans = "";

void done(int n, char p1, char p2) {
	if (n == 1) {
		ans.push_back(p1);
		ans.push_back(p2);
		return;
	}
	if (p1 == 'R') {
		done(n - 1, p1, 'S');
	}
	if (p1 == 'P') {
		done(n - 1, p1, 'R');
	}
	if (p1 == 'S') {
		done(n - 1, 'P', p1);
	}
	if (p2 == 'R') {
		done(n - 1, p2, 'S');
	}
	if (p2 == 'P') {
		done(n - 1, p2, 'R');
	}
	if (p2 == 'S') {
		done(n - 1, 'P', p2);
	}
}


void print(string &ans, int len) {
	if (len >= ans.size()) {
		for (int i = 0; i < ans.size(); i++) {
			cout << ans[i];
		}
		return;
	}
	for (int i = 0; i < ans.size(); i += 2 * len) {
		string s1 = "";
		string s2 = "";
		for (int j = i; j < i + len; j++) {
			s1 += ans[j];
			s2 += ans[j + len];
		}
		if (s2 < s1) {
			for (int j = i; j < i + len; j++) {
				swap(ans[j], ans[j + len]);
			}
		}
	}
	print(ans, len * 2);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin.tie(0);
	ios_base::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n, r, p, s;
		ans.clear();
		cout << "Case #" << i + 1 << ": ";
		cin >> n >> r >> p >> s;
		int r1 = 1, p1 = 0, s1 = 0;
		can(n, r1, p1, s1, 'R', 'P');
		if (r1 == r && p1 == p && s1 == s) {
			done(n, 'P', 'R');
			print(ans, 1);
			cout << '\n';
			continue;
		}
		r1 = 1, p1 = 0, s1 = 0;
		can(n, r1, p1, s1, 'R', 'S');
		if (r1 == r && p1 == p && s1 == s) {
			done(n, 'R', 'S');
			print(ans, 1);
			cout << '\n';
			continue;
		}
		r1 = 0, p1 = 1, s1 = 0;
		can(n, r1, p1, s1, 'P', 'S');
		if (r1 == r && p1 == p && s1 == s) {
			done(n, 'P', 'S');
			print(ans, 1);
			cout << '\n';
			continue;
		}
		cout << "IMPOSSIBLE\n";
	}



	return 0;
}