#include <algorithm>
#include <cstdio>

using namespace std;

const int MAXN = 11111;

int cs, a[MAXN];

inline void work() {
    int n, x;
    scanf("%d%d", &n, &x);
    for (int i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    sort(a, a + n);
    int ans = n;
    for (int i = n - 1, j = 0; j < i; --i)
        if (a[i] + a[j] <= x)
            ++j, --ans;
    printf("Case #%d: %d\n", ++cs, ans);
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--)
        work();
    return 0;
}
