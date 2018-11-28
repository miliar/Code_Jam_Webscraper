#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#define MAXN 4000
using namespace std;
int num[MAXN];
int vis[MAXN];
int judge[MAXN];
int c, d, v;
void dfs(int now) {
    if(now >= d) {
        int res = 0;
        for(int i = 0; i < d; i++) {
            if(vis[i]) {
                res += num[i];
            }
        }
        judge[res] = 1;
        return;
    }
    vis[now] = 1;
    dfs(now + 1);
    vis[now] = 0; dfs(now + 1);
}
int main() {
    freopen("in.in", "r", stdin);
    freopen("Cout.out", "w", stdout);
    int t;
    int ans;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++) {
        ans = 0;
        scanf("%d%d%d", &c, &d, &v);
        memset(vis, 0, sizeof(vis));
        memset(judge, 0, sizeof(judge));
        for(int i = 0; i < d; i++) {
            scanf("%d", &num[i]);
            judge[num[i]] = 1;
        }
        dfs(0);
        while(true) {
            vector <int> tt;
            tt.clear();
            int x = -1;
            for(int i = 1; i <= v; i++) {
                if(judge[i] == 0) {
                    x = i;
                    break;
                }
            }
            if(x == -1) break;
            ans++;
            tt.push_back(x);
            for(int i = 1; i <= v; i++) {
                if(judge[i]) {
                    tt.push_back(i + x);
                }
            }
            for(int i = 0; i < tt.size(); i++) {
                judge[tt[i]] = 1;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}

