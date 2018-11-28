#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

const int mo = 1000000007;
int n, m, T, test, ans, ti;
char s[1010][110];
int v[10], head[10];
int Trie[1000][26];

void check() {
	int val = 0, cnt = 0;
	memset(Trie, 0, sizeof(Trie));
	memset(head, 0, sizeof(head));
	for (int i = 0; i < n; ++i) {
		int len = strlen(s[i]), cur = head[v[i]];
		if (head[v[i]] == 0) head[v[i]] = cur = ++cnt; 
		for (int j = 0; j < len; ++j) {
			int ch = s[i][j] - 'A';
			if (Trie[cur][ch] == 0) Trie[cur][ch] = ++cnt;
			cur = Trie[cur][ch];
		}
	}
	if (cnt > ans) ans = cnt, ti = 1;
	else if (cnt == ans) ++ti;
}

void dfs(int x) {
	if (x == n) check();
	else {
		for (int i = 0; i < m; ++i) {
			v[x] = i;
			dfs(x + 1);
		}
	}
}

int main(){
	for (scanf("%d", &T), test = 1; test <= T; ++test) {
		scanf("%d %d\n", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", s[i]);
		ans = ti = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", test, ans, ti);
	}
}
