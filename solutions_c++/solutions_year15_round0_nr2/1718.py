#include <bits/stdc++.h>

using namespace std;

int jizz() {
    int n; scanf("%d", &n);

    vector<int> arr(n);

    for (int i = 0; i < n; ++i)
        scanf("%d", &arr[i]);

    sort(begin(arr), end(arr));

    int ans = arr[n-1];

    for (int maxv = 1; maxv < ans; ++maxv) {
        int cnt = 0;

        for (int i = n-1; i >= 0 and arr[i] > maxv; --i)
            cnt += (arr[i] - 1) / maxv;

        ans = min(ans, cnt + maxv);
    }

    return ans;
}

int main() {
    int T; scanf("%d", &T); for (int t = 1; t <= T; ++t)
        printf("Case #%d: %d\n", t, jizz());

    return 0;
}