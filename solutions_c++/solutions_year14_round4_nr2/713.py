#include <cstdio>
#include <algorithm>

int arr[1010];
int jizz() {
    int n;
    scanf("%d", &n)  ;

    for (int i = 0; i < n; ++i) {
        scanf("%d", &arr[i]);
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int mini = -1, minv = 1e9+2;
        for (int j = 0; j < n-i; ++j) {
            if (arr[j] < minv)
                minv = arr[j], mini = j;
        }

        for (int j = mini; j < n-i-1; ++j)
            arr[j] = arr[j+1];

        ans += std::min(n-i-1-mini, mini);
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
