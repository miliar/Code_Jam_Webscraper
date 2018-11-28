#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define N 1005

int n;
int a[N], p[N];
int b[N];

bool check() {
    for (int i = 0; i < n; ++i)
        b[i] = a[ p[i] ];
    int j = 0;
    while (j + 1 < n && b[j] < b[j + 1]) ++j;
    while (j + 1 < n && b[j] > b[j + 1]) ++j;
    return j == n - 1;
}

int cal() {
    copy(p, p + n, b);
    int res = 0;
    for (int i = 0; i < n; ++i) {
        int k = i;
        while (b[k] != i) ++k;
        for (int j = k; j > i; --j) {
            ++res;
            swap(b[j], b[j - 1]);
        }
    }
    return res;
}

int solve() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    for (int i = 0; i < n; ++i)
        p[i] = i;
    int ans = 1 << 30;
    do {
        if (check())
            ans = min(ans, cal());
    } while (next_permutation(p, p + n));
    return ans;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--)
        printf("Case #%d: %d\n", ++cas, solve());
    return 0;
}
