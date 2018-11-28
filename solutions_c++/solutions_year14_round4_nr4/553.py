#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <bitset>

typedef long long LL;
#define pb push_back
#define MPII make_pair<int, int>
#define PII pair<int, int>
#define sz(x) (int)x.size()

using namespace std;

template<class T> T abs(T x){if (x < 0) return -x; else return x;}

const int maxn = 100000;
int n, m, ans, total, root[maxn], belong[maxn];
char buf[10][maxn];

struct Node{
	int ch[26];
	void clear(){
		memset(ch, 0, sizeof(ch));
	}
}c[maxn];

void solve(){
	int tot = 0;
	for (int i = 0; i < m; ++i)
		root[i] = -1;
	for (int i = 0; i < n; ++i){
		if (root[belong[i]] == -1){
			++tot;
			root[belong[i]] = tot;
			c[tot].clear();
		}
		int u = root[belong[i]];
		for (int j = 0; j < strlen(buf[i]); ++j){
			int t = buf[i][j] - 'A';
			if (!c[u].ch[t]){
				++tot;
				c[u].ch[t] = tot;
				c[tot].clear();
			}
			u = c[u].ch[t];
		}
	}
	if (tot > ans){
		ans = tot;
		total = 1;
	} else	if (tot == ans) ++total;
}

void dfs(int u){
	if (u == n) {
		solve();
		return;
	}
	for (int i = 0; i < m; ++i){
		belong[u] = i;
		dfs(u + 1);
	}	
}

int main(){
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int C = 1; C <= Cases; ++C){
		printf("Case #%d: ", C);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
			scanf("%s", buf[i]);
		ans = 0;
		total = 0;
		dfs(0);
		printf("%d %d\n", ans, total);
	}
	return 0;
}

