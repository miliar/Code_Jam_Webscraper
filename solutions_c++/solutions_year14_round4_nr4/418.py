#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <vector>
using namespace std;

const int maxn = 10;
const int maxl = 15;

int ans, cnt;
struct node
{
	int net[26];
} tr[maxn][maxn * maxl];
char ch[maxn][maxl];
int b[maxn], n, m, nd[maxn];

void clear(int t, int tot)
{
	for (int i = 0; i != 26; i++) {
		tr[t][tot].net[i] = 0;
	}
}

void add(int t, char * st)
{
	int r = 0, c;
	for (int i = 0; i != strlen(st); i++) {
		c = st[i] - 'A';
		if (tr[t][r].net[c] == 0) {
			tr[t][r].net[c] = ++nd[t];
			clear(t, nd[t]);
		}
		r = tr[t][r].net[c];
	}
}

void dfs(int u)
{
	if (u > n) {
		for (int i = 1; i <= m; i++) {
			nd[i] = 0;
			clear(i, 0);
		} 
		for (int i = 1; i <= n; i++) add(b[i], ch[i]);
		int tmp = 0;
		for (int i = 1; i <= m; i++) {
			tmp += nd[i] + 1;
			if (nd[i] == 0) {
				tmp = 0;
				break;
			}
		}
		if (tmp > ans) {
			ans = tmp;
			cnt = 1;
		} else 
		if (tmp == ans) {
			++cnt;
		}
	} else {
		for (int i = 1; i <= m; i++) {
			b[u] = i;
			dfs(u + 1);
		}
	}
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int TextN;
	scanf("%d", &TextN);
	for (int TT = 1; TT <= TextN; TT++) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++) {
			scanf("%s", ch[i]);
		}
		ans = cnt = 0;
		dfs(1);
		printf("Case #%d: %d %d\n", TT, ans, cnt);
	}
}