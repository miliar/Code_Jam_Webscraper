#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

int n, a[3], c[3];

string ans;

void up(string t) {
    for(int i = 0; i < 3; ++ i) {
        if(a[i] != c[i])
            return;
    }
    if(ans.empty()) ans = t;
    else if(ans > t) ans = t;
}

char ch[] = "RPS";

string dfs(int n, int w) {
    if(n == 0) {
        ++ c[w];
        string t = "";
        t += ch[w];
        return t;
    }
    if(w == 0) {
        string a = dfs(n - 1, 0);
        string b = dfs(n - 1, 2);
        if(a < b) return a + b;
        return b + a;
    } else if(w == 1) {
        string a = dfs(n - 1, 1);
        string b = dfs(n - 1, 0);
        if(a < b) return a + b;
        return b + a;
    } else {
        string a = dfs(n - 1, 2);
        string b = dfs(n - 1, 1);
        if(a < b) return a + b;
        return b + a;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("Al.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++ cas) {
        scanf("%d%d%d%d", &n, &a[0], &a[1], &a[2]);
        ans.clear();
        memset(c, 0, sizeof(c));
        up(dfs(n, 0));
        memset(c, 0, sizeof(c));
        up(dfs(n, 1));
        memset(c, 0, sizeof(c));
        up(dfs(n, 2));
        if(ans.empty()) ans = "IMPOSSIBLE";
        printf("Case #%d: %s\n", cas, ans.c_str());
    }
    return 0;
}
