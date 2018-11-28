#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
using namespace std;

const int MAXN = 30;

int m, n;
int key_required[MAXN];
int my_keys[100];
vector<int> keys_contained[MAXN];
int f[1 << 20], can_open[1 << 20][20];
int key_count[201], my_key_count[201];

int main() {
    int tott;
    scanf("%d", &tott);
    for (int curt = 0; curt < tott; ++curt) {
        scanf("%d%d", &m, &n);
        memset(can_open, 0, sizeof can_open);
        memset(my_key_count, 0, sizeof(my_key_count));
        for (int i = 0; i < m; ++i) {
            scanf("%d", &my_keys[i]);
            ++my_key_count[my_keys[i]];
        }
        for (int i = 0; i < n; ++i) {
            int count, tmp;
            scanf("%d%d", &key_required[i], &count);
            for (int j = 0; j < count; ++j) {
                scanf("%d", &tmp);
                keys_contained[i].push_back(tmp);
            }
        }
        memset(f, 0xff, sizeof f);
        f[(1 << n) - 1] = 1;
        for (int i = (1 << n) - 2; i >= 0; --i) {
            memcpy(key_count, my_key_count, sizeof key_count);
            for (int j = 0; j < n; ++j) {
                if (1 << j & i) {
                    for (int k = 0; k < (int)keys_contained[j].size(); ++k) {
                        ++key_count[keys_contained[j][k]];
                    }
                }
            }
            int valid = 1;
            for (int j = 0; j < n; ++j) {
                if ((1 << j & i) && --key_count[key_required[j]] < 0) {
                    valid = 0;
                    break;
                }
            }
            if (valid) {
                f[i] = 0;
                for (int j = 0; j < n; ++j) {
                    if (!(1 << j & i) && key_count[key_required[j]]) {
                        can_open[i][j] = true;
                        f[i] |= f[i | (1 << j)];
                    }
                }
            }
        }
        
        printf("Case #%d:", curt + 1);
        if (!f[0]) {
            puts(" IMPOSSIBLE");
        } else {
            vector<int> ans;
            int opened = 0;
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (1 << j & opened) {
                        continue;
                    }
                    if (f[(1 << j) | opened] && can_open[opened][j]) {
                        ans.push_back(j + 1);
                        opened |= 1 << j;
                        break;
                    }
                }
            }
            for (int i = 0; i < n; ++i) {
                printf(" %d", ans[i]);
            }
            printf("\n");
        }

        // clean
        fill(keys_contained, keys_contained+MAXN, vector<int>());
    }
    return 0;
}

