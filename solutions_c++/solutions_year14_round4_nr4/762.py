//#pragma comment(linker,"/STACK:1024000000,1024000000")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <cstdlib>
#include <queue>
#include <stack>
#include <utility>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
typedef long  long LL;

const int N = 10005;
const int M = 1000005;
const int inf = 1 << 28;
const int mod = 1e9 + 7;
const double eps = 1e-8;
using namespace std;
int m, n;

struct node {
    int nx[26];
};

struct tire{
    node tree[N];
    int tot;
    void init() {
        tot = 0;
        for (int i = 0; i < 26; i++) tree[0].nx[i] = -1;
    }
    void build(int rt,int c) {
        ++tot;
        for (int i = 0; i < 26; i++) tree[tot].nx[i] = -1;
        tree[rt].nx[c] = tot;
    }
    void insert(char *s) {
        int len = strlen(s), i = 0, rt = 0;
        while (i < len) {
            int c = s[i] - 'A';
            i ++;
            if (tree[rt].nx[c] == -1)  build(rt, c);
            rt = tree[rt].nx[c];
        }
    }
}xdp[10];

int id[N];
char s[100][100];
int res, ans;

void cal() {
    for (int i = 0; i < n; i++) xdp[i].init();
    for (int i = 0; i < m; i++) {
        xdp[id[i]].insert(s[i]);
    }
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        cnt += xdp[i].tot;
        if (xdp[i].tot == 0) return;
    }
    cnt += n;
    if (cnt > res) {
        res = cnt, ans = 1;
    }else if (cnt == res) ans ++, ans %= mod;
}

void dfs(int k) {
    if (k == m) {
        cal();
        return;
    }
    for (int i = 0; i < n; i++) {
        id[k] = i;
        dfs(k + 1);
    }
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, cas = 1;
	cin >> T;
	while (T --) {
	    res = 0, ans = 0;
	    cin >> m >> n;
	    for (int i = 0; i < m; i++) {
            scanf("%s", s[i]);
	    }
	    dfs(0);
        printf("Case #%d: %d %d\n", cas ++, res, ans);
	}
	return 0;
}











