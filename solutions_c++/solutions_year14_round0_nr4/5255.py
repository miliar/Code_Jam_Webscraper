#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 1000;
double naomi[maxn];
double ken[maxn];

int main()
{
    int T, kase = 1;
    scanf("%d", &T);

    while (T--) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) scanf("%lf", naomi+i);
        for (int i = 0; i < n; ++i) scanf("%lf", ken+i);
        sort(naomi, naomi+n);
        sort(ken, ken+n);
        int cnt = 0, idx_nbeg = 0, idx_nend = n-1, idx_kend = n-1;
        while (true) {
            if (naomi[idx_nend] < ken[idx_kend]) {
                ++idx_nbeg;
                --idx_kend;
                ++cnt;
                continue;
            }
            if (naomi[idx_nend] > ken[idx_kend]) {
                --idx_nend;
                --idx_kend;
                continue;
            }
            if (idx_kend < 0) break;
        }
        int dw_win = n - cnt;
        cnt = 0;
        int idx_kbeg = 0;
        idx_kend = n-1;
        for (int i = n-1; i >= 0; --i) {
            if (naomi[i] < ken[idx_kbeg]) break;
            if (naomi[i] > ken[idx_kend]) {
                ++cnt;
                ++idx_kbeg;
            } else {
                auto it = upper_bound(ken + idx_kbeg, ken + idx_kend + 1, naomi[i]);
                rotate(it, it+1, ken + idx_kend + 1);
                --idx_kend;
            }
        }
        printf("Case #%d: %d %d\n", kase++, dw_win, cnt);
    }
}

