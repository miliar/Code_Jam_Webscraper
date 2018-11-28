#include <cstdio>
#include <algorithm>
using namespace std;
int arr[1000];
int main() {
    int tests;
    scanf("%d", &tests);
    for (int t = 1; t <= tests; t++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
        }
        int ans = 10000000;
        for (int last = 1; last <= 1000; last++) {
            int now = last;
            for (int i = 0; i < n; i++) {
                if (arr[i] > last) {
                    now += (arr[i] - 1) / last;
                }
            }
            ans = min(ans, now);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}

