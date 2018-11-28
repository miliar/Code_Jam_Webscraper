#include <algorithm>
#include <cstdio>
#include <cstring>
#include <set>
using namespace std;

int n;
char A[32][32];
char a[32][32];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", A[i]);
        }
        int bsol = n * n;
        for (int ma = 0; ma < (1 << (n * n)); ++ma) {
            if (__builtin_popcount(ma) >= bsol) {
                continue;
            }
            memcpy(a, A, sizeof(a));
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < n; ++j) {
                    if (ma & (1 << (n * i + j))) {
                        a[i][j] = '1';
                    }
                }
            }
            bool mask_ok = true;
            for (int i = 0; i < n; ++i) {
                bool can_block = true;
                for (int k = 0; k < (1 << n); ++k) {
                    bool ok = true;
                    for (int j = 0; j < n; ++j) {
                        if (a[i][j] == '0' && (k & (1 << j))) {
                            ok = false;
                        }
                    }
                    if (!ok) {
                        continue;
                    }
                    set<int> nb;
                    for (int j = 0; j < n; ++j) {
                        if (k & (1 << j)) {
                            for (int l = 0; l < n; ++l) {
                                if (l == i) {
                                    continue;
                                }
                                if (a[l][j] == '1') {
                                    nb.insert(l);
                                }
                            }
                        }
                    }
                    if ((int) nb.size() < __builtin_popcount(k)) {
                        can_block = false;
                    }
                }
                if (can_block) {
                    mask_ok = false;
                }
            }
            if (mask_ok) {
                bsol = __builtin_popcount(ma);
            }
        }
        printf("Case #%d: %d\n", t, bsol);
    }
    return 0;
}
