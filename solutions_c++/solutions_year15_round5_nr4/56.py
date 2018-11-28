#include <bits/stdc++.h>
using namespace std;

int e[10010], cnt[10010];
map<int, int> mp;
int a[100];

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &e[i]);
        }
        mp.clear();
        for (int i = 0; i < n; i++) {
            scanf("%d", &cnt[i]);
            mp[e[i]] = cnt[i];
        }
        mp[e[0]]--;
        int all = 0;
        while (true) {
            bool sol = false;
            int val = -1;
            for (auto v : mp) {
                if (v.second != 0) {
                    sol = true;
                    val = v.first;
                    break;
                }
            }
            if (!sol) {
                break;
            }
            a[all] = val;
            for (int i = 0; i < (1 << all); i++) {
                int sum = 0;
                for (int j = 0; j < all; j++) {
                    if (i & (1 << j)) {
                        sum += a[j];
                    }
                }
                mp[val + sum]--;
            }
            all++;
        }
        printf("Case #%d:", cas);
        for (int i = 0; i < all; i++) {
            printf(" %d", a[i]);
            fprintf(stderr, "%d ", a[i]);
        }
        puts("");
        fprintf(stderr, "\n");
    }
    return 0;
}