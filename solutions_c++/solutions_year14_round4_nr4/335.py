#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
char s[10][100];
int id[105];
int n, m;
vector<int> v[5];

const int N = 1029;
int next[N][26];
int L, root;
int newNode() {
	for (int i = 0; i < 26; ++i)
		next[L][i] = -1;
	return L++;
}
void init() {
	L = 0;
	root = newNode();
}
void insert(char *s) {
	int now = root;
	for (int i = 0; s[i]; ++i) {
		int ch = s[i] - 'A';
		if (next[now][ch] == -1)
			next[now][ch] = newNode();
		now = next[now][ch];
	}
}
int check() {
	int i, j, k;
	int ret = 0;
	for (i = 0; i < m; ++i) {
		if (v[i].empty())
			return -1;
		init();
		for (int j = 0; j < v[i].size(); ++j)
			insert(s[v[i][j]]);
		ret += L;
	}
	return ret;
}
int mx, cnt;
void dfs(int i) {
	int j;
	if (i == n) {
		int t = check();
		if (mx < t) {
			mx = t;
			cnt = 1;
		} else if (mx == t)
			cnt++;
		return;
	}
	for (j = 0; j < m; ++j) {
		v[j].push_back(i);
		dfs(i + 1);
		v[j].pop_back();
	}
}
int main() {
	int i;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; ++i) {
			scanf("%s", s[i]);
		}
		mx = -1;
		cnt = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", cas, mx, cnt);
	}
}
