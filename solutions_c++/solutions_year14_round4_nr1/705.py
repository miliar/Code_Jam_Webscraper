#include <cstdio>
#include <algorithm>

int arr[1000000];
int jizz() {
    int n;
    scanf("%d", &n);

    int x;
    scanf("%d", &x);

    for (int i = 0; i < n; ++i)
        scanf("%d", &arr[i]);

    std::sort(arr, arr + n);

    int ans = n, l = 0, r = n / 2, m;
    while (l <= r) {
        m = (l + r) / 2;

        bool jizz = true;
        for (int i = 0; i < m; ++i)
            jizz &= arr[i] + arr[m+m-1-i] <= x;

        if (jizz) ans = n - m, l = m + 1;
        else r = m - 1;
    }

    return ans;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 0; t < T; ++t) {
        printf("Case #%d: %d\n", t+1, jizz());
    }

    return 0;
}
