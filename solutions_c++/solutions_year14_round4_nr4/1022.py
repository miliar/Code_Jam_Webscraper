#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))

int m, n;
int g[10];
vector<string> S;
int ans1, ans2;

void go(int cnt) {
    if (cnt == m) {
        int gc[10] = {0};
        for (int i = 0; i < m; ++i) {
            gc[g[i]]++;
        }
        for (int i = 0; i < n; ++i) {
            if (gc[i] == 0) {
                return;
            }
        }

        set<string> chk[5];
        for (int i = 0; i < m; ++i) {
            int group = g[i];
            for (int j = 0; j < sz(S[i]); ++j) {
                chk[group].insert(S[i].substr(0, j + 1));
            }
        }

        int total = 0;
        for (int i = 0; i < n; ++i) {
            total += sz(chk[i]) + 1;
        }
        if (total > ans1) {
            ans1 = total;
            ans2 = 1;
        } else if (total == ans1) {
            ans2++;
        }
        return;
    }
    for (int i = 0; i < n; ++i) {
        g[cnt] = i;
        go(cnt + 1);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cs = 1; cs <= T; ++cs) {
        printf("Case #%d: ", cs);
        scanf("%d %d", &m, &n);
        S.clear();
        for (int i = 0; i < m; ++i) {
            char tmp[100];
            scanf("%s", tmp);
            S.push_back(tmp);
        }
        ans1 = ans2 = 0;
        go(0);
        printf("%d %d\n", ans1, ans2);
    }
    return 0;
}


