#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
using namespace std;
int t, n;
char buf[100020];
vector<int>a[220];
map<string, int>g;
int G(const string &s) {
	if (g.count(s) == 0) {
		int t = g.size();
		g[s] = t;
	}
	return g[s];
}

void readsen(vector<int> &a) {
	a.clear();
	gets(buf);
	istringstream iss(buf);
	string s;
	while(iss >> s) {
		a.push_back(G(s));
	}
}

int E[100020];
int F[100020];

int cnt, ans;

void dfs(int x) {
	if (x == n) {
		int cnt = 0;
		for (int i = 0; i < g.size(); i++) {
			if (E[i] && F[i]) {
				cnt += 1;
			}
		}
		if (ans > cnt) {
			ans = cnt;
		}
	} else {
		for (int i: a[x]) {
			E[i] += 1;
		}
		dfs(x + 1);
		for (int i: a[x]) {
			E[i] -= 1;
		}
		for (int i: a[x]) {
			F[i] += 1;
		}
		dfs(x + 1);
		for (int i: a[x]) {
			F[i] -= 1;
		}
	}
}

int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		ans = 1 << 30;
		memset(E, 0, sizeof E);
		memset(F, 0, sizeof F);
		g.clear();
		scanf("%d ", &n);
		for (int i = 0; i < n; i++) {
			readsen(a[i]);
		}
		for (int i: a[0]) {
			E[i] += 1;
		}
		for (int i: a[1]) {
			F[i] += 1;
		}
		dfs(2);
		printf("Case #%d: %d\n", tt, ans);
		
	}
	return 0;
}