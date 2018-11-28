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

int main() {
    int cnt_case = 0;
    scanf("%d", &cnt_case);
    int case_idx = 0;
    while (cnt_case--) {
        ++case_idx;

        // compute here
        int a,b,k;
        scanf("%d %d %d", &a, &b ,&k);
        int ans = 0;
        for (int l = 0; l < k; ++l) {
            for (int i = 0; i < a; ++i) {
                for (int j = 0; j < b; ++j) {
//                    printf("ans: %d %d %d i&j=%d %d\n", l, i, j, i&j, (i&j)==l);
                    if ((i & j) == l) {
                        ++ans;
                    }
                }
            }
        }

        printf("Case #%d: ", case_idx);
        printf("%d\n", ans);
        // output here
    }
    return 0;
}
