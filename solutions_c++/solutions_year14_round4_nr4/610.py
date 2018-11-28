#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
using namespace std;

int calc(vector <string> s) {
	sort(s.begin(), s.end());
	int res = 1;
	for (string& ss : s)
		res += ss.length();
	for (size_t i = 1; i < s.size(); i++) {
		string& a = s[i - 1];
		string& b = s[i];
		int l = 0;
		while (l < a.size() && a[l] == b[l])
			l++;
		res -= l;
	}
	return res;
}

vector <string> t[4];
vector <string> s;

int best;
int vars;

void solve(int i, int m) {
	if (s.size() == i) {
		for (int j = 0; j < m; j++)
			if (t[j].size() == 0)
				return;
		int cur = 0;
		for (int j = 0; j < m; j++)
			cur += calc(t[j]);
		if (cur < best)
			return;
		if (cur > best) {
			best = cur;
			vars = 1;
			return;
		}
		vars++;
		return;
	}
	for (int j = 0; j < m; j++) {
		t[j].push_back(s[i]);
		solve(i + 1, m);
		t[j].pop_back();
	}
}

void solve() {
	best = 0;
	vars = 0;
	int n, m;
	cin >> n >> m;
	s.resize(n);
	for (string& i : s)
		cin >> i;
	solve(0, m);
	printf("%d %d\n", best, vars);
}


int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++){
		printf("Case #%d: ", test);
		solve();
	}
}