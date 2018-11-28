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
int n, m;
int a[10];
bool flag[10];
char s[10][10];
char ans[800];
char tmp[800];
bool f;
int gg[10][10];
void check() {
	int i;
	int sta[10], ed;
	ed = 0;
	sta[ed++] = a[0];
	for (i = 1; i < n; ++i) {
		while (ed > 0 && gg[sta[ed - 1]][a[i]] == 0)
			ed--;
		if (ed == 0)
			return;
		sta[ed++] = a[i];
	}
	tmp[0] = 0;
	for (i = 0; i < n; ++i) {
		strcat(tmp, s[a[i]]);
	}
	if (f == false) {
		strcpy(ans, tmp);
		f = true;
	} else {
		if (strcmp(ans, tmp) > 0)
			strcpy(ans, tmp);
	}
}
void dfs(int k) {
	int j;
	if (k == n) {
		check();
		return;
	}
	for (j = 0; j < n; ++j) {
		if (flag[j]) {
			flag[j] = false;
			a[k] = j;
			dfs(k + 1);
			flag[j] = true;
		}
	}
}
int main() {
	int i, j, k;
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; ++i)
			scanf("%s", s[i]);
		memset(gg, 0, sizeof(gg));
		for (i = 0; i < m; ++i) {
			scanf("%d%d", &j, &k);
			j--;
			k--;
			gg[j][k] = gg[k][j] = 1;
		}
		f = false;
		memset(flag, true, sizeof(flag));
		dfs(0);
		printf("Case #%d: %s\n", cas, ans);
	}
}
