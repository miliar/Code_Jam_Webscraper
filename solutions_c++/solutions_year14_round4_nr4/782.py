#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;

typedef long long ll;
const int N = 111111;
int trie[111111][26];
char s[11][111];
int nn, n, m, ans1, ans2;
int id[111];
vector<int> ss[111];

void insert(int rt, int k) {
	int len = strlen(s[k]);
	for (int i=0; i<len; ++i) {
		int now = s[k][i] - 'A';
		if (!trie[rt][now]) {
			++nn;
			trie[rt][now] = nn;
			memset(trie[nn], 0, sizeof(trie[nn]));
		}
		rt = trie[rt][now];
	}
}

int chk() {
	for (int i=0; i<m; ++i) {
		ss[i].clear();
	}
	for (int i=0; i<n; ++i) {
		ss[id[i]].push_back(i);
	}
	for (int i=0; i<m; ++i) {
		if (ss[i].size() == 0) return 0;
	}
	nn = m;
	for (int i=0; i<m; ++i) {
		memset(trie[i], 0, sizeof(trie[i]));
		for (int j=0; j<ss[i].size(); ++j) {
			insert(i, ss[i][j]);
		}
	}
	return nn;
}

void dfs(int deep) {
	//cout << deep << endl;
	if (deep == n) {
		int cal = chk();
		if (cal > ans1) {
			ans1 = cal;
			ans2 = 1;
		} else {
			if (cal == ans1) {
				ans2 ++;
			}
		}
		return ;
	}
	for (int i=0; i<m; ++i) {
		id[deep] = i;
		dfs(deep + 1);
	}
}

int main() {
	int _, cas = 0;
	scanf("%d", &_);
	while (_--) {
		scanf("%d%d", &n, &m);

		for (int i=0; i<n; ++i) {
			scanf("%s", s[i]);
		}
		ans1 = ans2 = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", ++cas, ans1, ans2);
	}
	return 0;
}