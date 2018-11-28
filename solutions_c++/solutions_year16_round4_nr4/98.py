#include <bits/stdc++.h>

using namespace std;

const int Inf = 1e9 + 7;

int T, cas, n, a[5][5], b[5][5], vis[5];

char ch[5];

vector<int> v;

bool Dfs(int cur) {
    if (cur == n) return true;
    bool flag = 0;
    for (int i = 0; i < n; i ++) {
        if (b[v[cur]][i] && vis[i] == 0) {
            flag = 1;
            vis[i] = true;
            if (!Dfs(cur + 1)) return false;
            vis[i] = false;
        }
    }
    return flag;
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    while (T --) {
        cin >> n;
        int mask = 0;
        for (int i = 0; i < n; i ++) {
            scanf(" %s", &ch);
            for (int j = 0; j < n; j ++) {
                a[i][j] = ch[j] - '0';
                mask |= (a[i][j] << (i * n + j));
            }
        }
        int res = 1e9;
        for (int i = 0; i < 1 << (n * n); i ++) {
            if (i & mask) continue;
            for (int j = 0; j < n; j ++){
                for (int k = 0; k < n; k ++){
                    b[j][k] = (a[j][k] | (i >> (j * n + k) & 1));
//                    cout << b[j][k];
                }
//                cout << endl;
            }

            int cnt = 0;
            for (int j = 0; j < n * n; j ++)
                if (i >> j & 1) cnt ++;
//            cout << i << ' ' << mask << ' ' << cnt << endl;
            v.clear();
            for (int j = 0; j < n; j ++)
                v.push_back(j);
            bool flag = 0;
            do {
                memset(vis, 0, sizeof(vis));
                if (!Dfs(0)) {
                    flag = 1;
                    break;
                }
            } while (next_permutation(v.begin(), v.end()));
            if (flag == 0) {
                res = min(res, cnt);
            }
        }
        printf("Case #%d: %d\n", ++ cas, res);
    }
}
