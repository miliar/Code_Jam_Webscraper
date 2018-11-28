#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxN = 1005;

int f[maxN], n, res, m;
vector <int> tmp;
int id[maxN], head[maxN];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int nTests = 0;
    scanf("%d", &nTests);
    for(int Case = 1; Case <= nTests; ++Case) {
        printf("Case #%d: ", Case);

        scanf("%d", &n);
        for(int i = 1; i <= n; ++i) scanf("%d", &f[i]);

        res = 1;

        for(int bit = (1 << n) - 1; bit > 0; --bit) {
            tmp.clear();
            for(int i = 1; i <= n; ++i)
                if (bit & (1 << (i - 1))) tmp.push_back(i);

            bool check = true;

            m = tmp.size();

            if (tmp.size() <= res) continue;

            for(int i = 0; i < m; ++i) {
                int v = f[tmp[i]];
                bool ok = false;
                for(int j = 0; j < m; ++j)
                    if (tmp[j] == v) {
                        ok = true;
                        break;
                    }
                if (!ok) {
                    check = false;
                    break;
                }
            }

            if (check) {
                for(int i = 1; i <= m; ++i) id[i] = i;

                do {
                    for(int i = 1; i <= m; ++i) head[i-1] = tmp[id[i] - 1];
                    bool ok = true;
                    for(int i = 0; i < m; ++i) {
                        int l = (i == 0 ? m - 1 : i - 1);
                        int r = (i == m - 1 ? 0 : i + 1);
                        if (f[head[i]] != head[l] && f[head[i]] != head[r]) {
                            ok = false;
                            break;
                        }
                    }
                    if (ok) {
                        res = max(res, m);
                        break;
                    }
                } while (next_permutation(id + 1, id + m + 1));
            }
        }

        printf("%d\n", res);
    }

    return 0;
}

