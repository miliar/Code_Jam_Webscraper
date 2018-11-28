#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <algorithm>

using namespace std;

const int MAXN = 10;

int m, n;
string s[MAXN];
char buf[20];
int p[MAXN];
int res;
int cnt;

int calc_trie(set<string> ss) {
	set<string> t;
	t.insert("");
	for (set<string>::iterator it = ss.begin(); it != ss.end(); it++) {
		string cur = *it;
		for (int i = 0; i < cur.size(); ++i)
			t.insert(cur.substr(0, i + 1));
	}
	return t.size();
}

int calc() {
	int res = 0;
	for (int j = 0; j < n; ++j) {
		set<string> cur;
		for (int i = 0; i < m; ++i) {
			if (p[i] == j)
				cur.insert(s[i]);
		}
		if (cur.size() == 0)
			return -1;
		res += calc_trie(cur);
	}
	return res;
}

void rec(int index) {
	if (index == m) {
		int curc = calc();
		if (curc == -1)
			return;
		if (curc > res) {
			res = curc;
			cnt = 1;
		}
		else if (curc == res) {
			cnt++;
		}
		return;
	}
	for (int j = 0; j < n; ++j) {
		p[index] = j;
		rec(index + 1);
	}
}

void solve(int test_id) {
	cout << "Case #" << test_id << ": ";
	scanf("%d%d\n", &m, &n);
	for (int i = 0; i < m; ++i) {
		gets(buf);
		s[i] = string(buf);
	}

	res = 0; cnt = 0;
	rec(0);

	cout << res << " " << cnt << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int test_id = 1; test_id <= t; ++test_id)
		solve(test_id);
	return 0;
}
