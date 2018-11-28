#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 1000005;

int n, d, s[N], fa[N], as, cs, rs, am, cm, rm, l[N], r[N];

vector<int> edge[N];

void dfs(int u, int fa) {
    if (fa != -1) {
        l[u] = max(l[u], l[fa]);
        r[u] = min(r[u], r[fa]);
    }
    for (int i = 0; i < (int)edge[u].size(); ++i) {
        int v = edge[u][i];
        if (v == fa) {
            continue;
        }
        dfs(v, u);
    }
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &n, &d);
        for (int i = 0; i < n; ++i) {
            edge[i].clear();
        }
        scanf("%d%d%d%d", &s[0], &as, &cs, &rs);
        scanf("%d%d%d%d", &fa[0], &am, &cm, &rm);
        for (int i = 1; i < n; ++i) {
            s[i] = ((long long)s[i - 1] * as + cs) % rs;
            fa[i] = ((long long)fa[i - 1] * am + cm) % rm;
        }
        for (int i = 1; i < n; ++i) {
            fa[i] %= i;
            edge[fa[i]].push_back(i);
        }
        vector<pair<int, int> > sal;
        for (int i = 0; i < n; ++i) {
            sal.push_back(make_pair(s[i], i));
        }
        sort(sal.begin(), sal.end());
        /*
        for (int i = 0; i < (int)sal.size(); ++i) {
            printf("%d %d\n", sal[i].first, sal[i].second);
        }*/
        int target = n - 1;
        for (int i = n - 1; i >= 0; --i) {
            while (target > 0 && sal[i].first - sal[target - 1].first <= d) {
                --target;
            }
            l[sal[i].second] = target;
            r[sal[i].second] = i;
        }
        dfs(0, -1);
        vector<pair<int, int> > event;
        for (int i = 0; i < n; ++i) {
            if (l[i] <= r[i]) {
                event.push_back(make_pair(l[i], -1));
                event.push_back(make_pair(r[i], 1));
            } 
        }
        sort(event.begin(), event.end());
        int ans = 0, cnt = 0;
        for (int i = 0; i < (int)event.size(); ++i) {
            cnt -= event[i].second;
            ans = max(ans, cnt);
        }
        static int id = 0;
        printf("Case #%d: %d\n", ++id, ans);
    }
    return 0;
}
