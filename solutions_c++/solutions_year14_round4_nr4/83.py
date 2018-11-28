#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
using namespace std;

#define FOR(i,a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++ i)

const int maxn = 10 + 5;
const int maxm = 10 + 5;
const int maxlength = 10 + 5;

int n, m;
char word[maxm][maxlength];

int best = -1, answer = 0;
int trie[maxm * maxlength][26];

vector<int> server[maxn];

void dfs(int u)
{
	if (u == m) {
		int current = 0;
		for (int i = 0; i < n; ++ i) {
			int nodes = 0;
			memset(trie, 0, sizeof(trie));
			for (int j = 0; j < server[i].size(); ++ j) {
				char* s = word[server[i][j]];
				int cur = 0;
				for (int k = 0; s[k]; ++ k) {
					int ch = s[k] - 'A';
					if (trie[cur][ch] == 0) {
						trie[cur][ch] = ++ nodes;
					}
					cur = trie[cur][ch];
				}
			}
			if (server[i].size()) {
				current += nodes + 1;
			}
		}
		
		if (current > best) {
			best = current;
			answer = 0;
		}
		if (current == best) {
			answer += 1;
		}
		return;
	}
	for (int i = 0; i < n; ++ i) {
		server[i].push_back(u);
		dfs(u + 1);
		server[i].pop_back();
	}
}

void solve()
{
	scanf("%d%d", &m, &n);
	
	for (int i = 0; i < m; ++ i) {
		scanf("%s", word[i]);
	}
	
	best = -1;
	answer = 0;
	dfs(0);
	printf("%d %d\n", best, answer);
}

int main()
{
	int tests, test = 1;
	for (scanf("%d", &tests); test <= tests; ++ test) {
		printf("Case #%d: ", test);
		solve();
	}
	return 0;
}
