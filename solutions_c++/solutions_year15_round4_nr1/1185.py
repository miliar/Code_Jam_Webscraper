#include <cstdio>
#include <cstring>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <functional>
#include <utility>
#include <string>
#include <sstream>

using namespace std;

char ma[1100][1100];
int n, m;
vector<int> x[1100], y[1100];
vector<pair<int, int> > S;
int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= n; i++) x[i].clear();
        for (int j = 1; j <= m; j++) y[j].clear();
        S.clear();
        for (int i = 1; i <= n; i++) {
            scanf("%s", ma[i] + 1);
            for (int j = 1; j <= m; j++) {
                if (ma[i][j] != '.') {
                    x[i].push_back(j);
                    y[j].push_back(i);
                    S.push_back(make_pair(i, j));
                }
            }
        }
        for (int i = 1; i <= n; i++) sort(x[i].begin(), x[i].end());
        for (int j = 1; j <= m; j++) sort(y[j].begin(), y[j].end());
               bool ok = 1;
        int ans = 0;
        for (int i = 0; i < S.size(); i++) {
            int a = S[i].first;
            int b = S[i].second;
            if (ma[a][b] == '<' || ma[a][b] == '>') {
                int p = lower_bound(x[a].begin(), x[a].end(), b) - x[a].begin();
                if (ma[a][b] == '<') {
                    if (p != 0)
                        continue;
                    else if (p+1 != x[a].size() || y[b].size() > 1) {
                        ans++;
                        continue;
                    }
                    else {
                        ok = 0;
                        break;
                    }
                }
                else {
                    if (p+1 != x[a].size()) continue;
                    else if (p != 0 || y[b].size() > 1) {
                        ans++;
                        continue;
                    }
                    else {
                        ok = 0;
                        break;
                    }
                }
            }
            else {
                int p = lower_bound(y[b].begin(), y[b].end(), a) - y[b].begin();
                if (ma[a][b] == '^') {
                    if (p != 0) {
                        continue;
                    }
                    else if (p+1 != y[b].size() || x[a].size() > 1) {
                        ans++;
                        continue;
                    }
                    else {
                        ok = 0;
                        break;
                    }
                }
                else {
                    if (p+1 != y[b].size()) continue;
                    else if (p != 0 || x[a].size() > 1) {
                        ans++;
                        continue;
                    }
                    else {
                        ok = 0;
                        break;
                    }
  
                }
            }
        }
        printf("Case #%d: ", kase);
        if (!ok) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
