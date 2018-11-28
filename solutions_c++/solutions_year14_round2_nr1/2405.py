#include <string>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const double kEPS = 1E-9;
const int kSize = 1024;

int cmp_asc(const void* p1, const void *p2) {
    return *(int*)p1 - *(int*)p2;
}

int cmp_desc(const void* p1, const void *p2) {
    return *(int*)p2 - *(int*)p1;
}

char strs[kSize][kSize];
int idxes[kSize];

int main() {
    int cnt_case = 0;
    scanf("%d", &cnt_case);
    int case_idx = 0;
    while (cnt_case--) {
        ++case_idx;
        memset(strs,0,sizeof(strs));
        memset(idxes,0,sizeof(idxes));

        // compute here
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", strs[i]);
        }

        int ans = 0;
        bool succ = false;
        while (true) {
            int i = 0;
            int cnt = 0;
            for (i = 0; i < n; ++i) {
                if (strs[i][idxes[i]] == '\0')
                    ++cnt;
            }

            if (cnt == n) {
                succ = true;
                break;
            }

            if (cnt != 0) {
                succ = false;
                break;
            }

            int same = 0;
            int dif = 0;
            for (i = 0; i < n; ++i) {
                if (strs[i][idxes[i]] != strs[0][idxes[0]]) {
                    break;
                }
                
                if (strs[i][idxes[i]] == strs[i][idxes[i] + 1]) {
                    ++same;
                } else {
                    ++dif;
                }
            }

            if (i != n) {
                succ = false;
                break;
            }

            if (same != 0 && dif != 0) {
                if (same >= dif) {
                    ans += dif;
                    for (int i = 0; i < n; ++i) {
                        if (strs[i][idxes[i]] == strs[i][idxes[i]+1])
                            ++idxes[i];
                    }
                } else {
                    for (int i = 0; i < n; ++i) {
                        if (strs[i][idxes[i]] != strs[i][idxes[i]+1]) {
                            ++idxes[i];
                        } else {
                            idxes[i] += 2;
                        }
                    }

                    ans += same;
                }
            } else {
                for (int i = 0; i < n; ++i) {
                    ++idxes[i];
                }
            }
        }

        printf("Case #%d: ", case_idx);
        if (succ) {
            printf("%d\n", ans);
        } else {
            printf("Fegla Won\n");
        }

        // output here
    }
    return 0;
}
