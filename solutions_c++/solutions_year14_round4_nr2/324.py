#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int vis[1010];
int main() {
    freopen("B-large (1).in", "r", stdin);
    freopen("BB_large.out", "w", stdout);
    int t, ca, n, v, i, j, k;
    vector< pair<int, int> > pts;
    scanf("%d", &t);
    for (ca = 1; ca <= t; ca ++ ) {
        scanf("%d", &n);
        pts.clear();
        memset(vis, 0, sizeof(vis));
        for(i = 0; i < n; i++)
        {
            scanf("%d", &v);
            pts.push_back(make_pair(v, i));
        }
        sort(pts.begin(), pts.end());
        int ans = 0;
        for (i = 0; i < n; i ++ ) {
            int left = 0, right = 0;
            vis[pts[i].second] = true;
            for (j = 0; j < n; j ++ )
                if (!vis[j]) {
                    if (j < pts[i].second) left++;
                    else right++;
                }
            ans += min(left, right);
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}

