#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#define POW2(k) (1<<(k))
#define POW2L(k) (1ULL<<(k))
#define INSIDE(a, b) (POW2(a) & (b))
#define MERGE(a, b) (POW2(a) | (b))
#define LOWBIT(v) ((v)&(-(v)))
#define INF 0x3f3f3f3f
#define EPS 1e-10
using namespace std;

const double PI = acos(-1.0);

typedef pair<int, int> pii;
typedef long long LL;
typedef unsigned long long ULL;

template<class T1, class T2> inline bool ChkMax(T1 &a, const T2 &b) { if (a < b) { a = b; return true; } return false; }
template<class T1, class T2> inline bool ChkMin(T1 &a, const T2 &b) { if (a > b) { a = b; return true; } return false; }

#define MAXN 1003
#define MAXL 103
#define MOD 1000000007

int m, n;
char str[1001][13];
int lab[1001];
bool slot[101];
int res, f_cnt;

int check(int cur) {
	set<string> tmp;
	for (int i = 0; i < m; i++) {
		if (lab[i] == cur) {
			for (int j = 0; j < strlen(str[i]); j++) {
				string s = str[i];
				tmp.insert(s.substr(0, j + 1));
			}
		}
	}
	return tmp.size() + 1;
}

void verify() {
	int ans = 0;
	for (int i = 0; i < n; i++) {
		ans += check(i);
	}

	if (ans == res) {
		f_cnt++;
	} else if (ans > res) {
		f_cnt = 1;
		res = ans;
	}
}

void dfs(int cur = 0, int cnt = 0)
{
	if (cur == m) {
		if (cnt == n) {
			verify();
		}
		return ;
	}
	for (int i = 0; i < n; i++) {
		lab[cur] = i;
		if (slot[lab[cur]] == false) {
			slot[lab[cur]] = true;
			dfs(cur + 1, cnt + 1);
			slot[lab[cur]] = false;
		} else {
			dfs(cur + 1, cnt);
		}
	}
}

void solve() {
	res = 0;
	f_cnt = 0;
	memset(slot, 0, sizeof(slot));
	dfs(0, 0);
	printf(" %d %d\n", res, f_cnt);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("D-small-attempt1.in", "r", stdin);
	// 	freopen("D-small-attempt0.in", "r", stdin);
 	freopen("out", "w", stdout);
#endif

	int dataset;
	scanf("%d", &dataset);
	for (int cas = 1; cas <= dataset; ++cas) {
		scanf("%d %d", &m, &n);
		for (int i = 0; i < m; ++i) {
			scanf("%s", str[i]);
		}
		printf("Case #%d:", cas);
		solve();
	}

	return 0;
}

